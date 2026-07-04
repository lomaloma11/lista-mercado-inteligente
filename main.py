import streamlit as st
import pandas as pd
import sqlalchemy as sa
import datetime
import json 
import time

import os 
import dotenv
dotenv.load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

EMAIL_ACESS = os.getenv("EMAIL_ACESS")

from gen_ai import generate

engine = sa.create_engine("sqlite:///database.db")

with open("query_inteligente.sql") as query_file:
    query = query_file.read()

with open("prompt_template.md") as prompt_file:
    prompt = prompt_file.read()

with open("resposta_template.json") as resposta_file:
    resposta = json.load(resposta_file)

@st.cache_data(ttl='10min')
def process_nf(prompt, resposta_template, produtos, img_file):
    st.image(img_file)

    promt_exec = prompt.format(produtos="\n".join(produtos), resposta=resposta_template)
    
    resp = generate(promt_exec, img_file.getvalue(), img_file.type)

    df = pd.DataFrame(json.loads(resp.text))
    return df

def get_produtos(engine):
    try:
        query_produtos = "SELECT DISTINCT produto FROM compras"
        df_produtos = pd.read_sql_query(query_produtos, engine)
        return df_produtos["produto"].tolist()
    except Exception as err:
        print(f"Erro ao consultar produtos: {err}")
        return []
    
def show_dt_compra(df:pd.DataFrame):

    df = df.sort_values(["comprar", "ultima_compra"], ascending=False)

    mostrar_tudo = st.checkbox("Mostrar todos os produtos", value=False)

    if not mostrar_tudo:
        df = df[df["comprar"]]

    columns_config = {
       "produto": st.column_config.TextColumn(label="Produto"),
       "ultima_compra": st.column_config.DateColumn(label="Última compra"),
       "valor_medio": st.column_config.NumberColumn(label="Valor Médio", format="R$ %.2f"),
       "avg_diffs_dias": st.column_config.NumberColumn(label="Intervalo entre as compras", format="%.2f"),
       "dias_ult_compra": st.column_config.NumberColumn(label="Dias desde a última compra", format="%.2f"),
       "comprar": st.column_config.CheckboxColumn(label="Comprar"),
    }
    st.dataframe(df, column_config=columns_config, hide_index=True)

    if df["comprar"].max() == 0:
        st.success(f"Não há produtos a serem comprados considerando os {numero_dias_adiante} dias de mercado")
    


st.set_page_config(page_title="Lista Inteligente", page_icon="🛒", layout="centered")

st.markdown("# Lista de compras inteligente!")

if not st.user.is_logged_in:
    if st.button("Log in"):
        st.login()

elif st.user.email != EMAIL_ACESS:
    st.warning("Usuário não autorizado. Por favor, entre com um email autorizado para acessar essa aplicação")
    time.sleep(1)
    st.logout()

else:

    try:
        col, _  = st.columns(2)
        numero_dias_adiante = col.number_input("Dias sem voltar ao mercado adiante", 
                                            min_value=0, 
                                            max_value=60, 
                                            step=1)
        df_stats = pd.read_sql_query(query, engine)

        if not df_stats.empty:
            df_stats["valor_medio"] = df_stats["valor_medio"].astype(float).round(2)
            df_stats["avg_diffs_dias"] = df_stats["avg_diffs_dias"].astype(float).round(1)
            df_stats["dias_ult_compra"] = df_stats["dias_ult_compra"].astype(float).round(1)
            
            df_stats["comprar"] = df_stats["dias_ult_compra"] + numero_dias_adiante > df_stats["avg_diffs_dias"]
            df_compra = df_stats[df_stats["comprar"]]
        else:
            df_compra = pd.DataFrame()

    except Exception as err:
        print(f"Erro ao consultar o banco: {err}")
        df_stats = pd.DataFrame()

    if df_stats.empty:
        st.warning("Não há dados históricos para exibir. Por favor, registre mais compras.")
        
    else:
        show_dt_compra(df_stats)

    st.markdown("## Adicionar novas compras")

    tab_produto, tab_historico, tab_nf = st.tabs(["Produto", "Histórico", "Nota Fiscal"])

    with tab_produto:
        produtos_unicos = get_produtos(engine)

        produto_selecionado = st.selectbox(
            "Produto", 
            options=["Novo Produto"] + produtos_unicos
        )

        if produto_selecionado == "Novo Produto":
            produto_final = st.text_input("Nome do novo produto").title()
        else:
            produto_final = produto_selecionado

        valor = st.number_input("Valor", min_value=0.01)

        if st.button("Registrar compra"):
            if not produto_final:
                st.error("Por favor, insira o nome do produto.")
            else:
                data = {
                    "dt_compra": datetime.datetime.now().strftime("%Y-%m-%d"),
                    "produto": produto_final,
                    "valor_produto": valor,
                }

                df_insert = pd.DataFrame([data])
                df_insert.to_sql("compras", engine, if_exists="append", index=False)
                st.success("Compra registrada com sucesso!")
                st.rerun()

    with tab_historico:
        st.markdown("### Importar histórico")

        open_file = st.file_uploader("Entre com um arquivo histórico", type=["csv"])

        if open_file:
            df = pd.read_csv(open_file)
            df = st.data_editor(df) 

            if st.button("Registrar dados", key="btn_registrar_csv"):
                df.to_sql("compras", engine, if_exists="append", index=False)
                st.success("Dados registrados com sucesso!")
                st.rerun()

    with tab_nf:
        st.markdown("### Importar Nota Fiscal")

        open_img = st.file_uploader("Entre com um arquivo de Nota Fiscal", type=["png", "jpeg"])

        if open_img:
            df = process_nf(prompt=prompt, resposta_template=resposta, produtos=produtos_unicos, img_file=open_img)
            df = st.data_editor(df)
            if st.button("Registrar dados", key="btn_registrar_nf"):
                df.to_sql("compras", engine, if_exists="append", index=False)
                st.success("Dados registrados com sucesso!")
                st.rerun()

    if st.button("Log out"):
        st.logout()
        
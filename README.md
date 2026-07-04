🛒 Lista de Compras Inteligente

Este é um projeto de aplicativo web construído com Streamlit e Inteligência Artificial (Google Gemini) para gerenciar compras de mercado. O objetivo principal do aplicativo não é apenas registrar produtos, mas sim analisar o histórico de compras para prever e recomendar o que precisa ser comprado antes de ir ao mercado.

Status do Projeto: Finalizado. Este projeto foi desenvolvido para fins de estudo e experimentação com IA generativa, processamento de dados e autenticação web.

🚀 Funcionalidades

Recomendação Inteligente: Calcula a média de dias entre as compras de cada produto e avisa se está na hora de comprar novamente, com base em quantos dias o usuário pretende ficar sem ir ao mercado.

Leitura de Nota Fiscal com IA: Permite o upload de imagens de notas fiscais (PNG/JPEG). O Google Gemini Vision analisa a imagem, extrai os itens comprados e seus valores, e os formata automaticamente para o banco de dados.

Importação em Lote: Suporte para upload de histórico de compras via arquivos .csv.

Inserção Manual: Interface simples para adicionar produtos e valores individualmente.

Autenticação Segura: Login integrado utilizando Google OAuth 2.0 de forma nativa pelo Streamlit.

Banco de Dados Local: Armazenamento do histórico em banco de dados SQLite, gerenciado via SQLAlchemy.

🛠️ Tecnologias Utilizadas

Python 3

Streamlit (Interface gráfica web e Autenticação OAuth)

Pandas (Tratamento e análise dos dados)

SQLAlchemy & SQLite (Modelagem e banco de dados relacional)

Google GenAI API (Extração de dados de imagens de Notas Fiscais)

📁 Estrutura do Projeto

main.py: Arquivo principal da aplicação Streamlit que contém a interface e a lógica de negócios.

gen_ai.py: Módulo responsável por fazer a comunicação com a API do Google Gemini e extrair os dados das imagens.

database.db: Banco de dados SQLite contendo a tabela de histórico de compras.

query_inteligente.sql: Script SQL com CTEs complexas para calcular a diferença de dias, médias de valores e gerar os dados estatísticos dos produtos.

prompt_template.md: Template do prompt enviado ao Gemini para instruí-lo a extrair os dados da nota fiscal no formato correto.

resposta_template.json: Estrutura de dados esperada como retorno da IA.

requirements.txt: Lista de dependências do projeto.

.streamlit/secrets.toml: Arquivo de configuração de credenciais OAuth (não versionado).

.env: Arquivo de variáveis de ambiente contendo a chave da API da IA (não versionado).

⚙️ Como executar o projeto localmente

Clone este repositório.

Crie um ambiente virtual e ative-o:

python -m venv .venv
source .venv/bin/activate  # Linux/Mac
.venv\Scripts\activate     # Windows


Instale as dependências:

pip install -r requirements.txt


Configure as variáveis de ambiente:

Crie um arquivo .env na raiz do projeto e adicione sua chave de API do Gemini:

GEMINI_API_KEY=sua_chave_aqui


Crie o arquivo .streamlit/secrets.toml para o OAuth do Google:

[auth]
redirect_uri = "http://localhost:8501/oauth2callback"
client_id = "seu_client_id_do_google_cloud.apps.googleusercontent.com"


Inicie a aplicação:

streamlit run main.py

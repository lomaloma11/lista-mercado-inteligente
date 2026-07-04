# 🛒 Lista de Compras Inteligente

Um aplicativo web desenvolvido com **Streamlit** e **Google Gemini** para gerenciar compras de mercado de forma inteligente.

Em vez de apenas registrar produtos, o sistema analisa o histórico de compras para prever quando cada item deverá ser comprado novamente, ajudando o usuário a planejar suas idas ao mercado.

> **Status:** ✅ Finalizado
> Projeto desenvolvido para fins de estudo e experimentação com Inteligência Artificial Generativa, análise de dados, autenticação web e desenvolvimento de aplicações em Python.

---

# 🚀 Funcionalidades

* 🧠 **Recomendação Inteligente**

  * Calcula a média de dias entre as compras de cada produto.
  * Recomenda quais itens precisam ser comprados novamente com base no período informado pelo usuário.

* 🧾 **Leitura de Nota Fiscal com IA**

  * Upload de imagens nos formatos **PNG** e **JPEG**.
  * Utiliza o **Google Gemini Vision** para identificar automaticamente os produtos e seus respectivos preços.

* 📂 **Importação em Lote**

  * Importação do histórico de compras através de arquivos **CSV**.

* ✍️ **Cadastro Manual**

  * Permite adicionar produtos individualmente pela interface.

* 🔐 **Autenticação**

  * Login utilizando **Google OAuth 2.0** integrado ao Streamlit.

* 💾 **Banco de Dados**

  * Armazenamento do histórico em **SQLite**, utilizando **SQLAlchemy**.

---

# 🛠️ Tecnologias Utilizadas

* Python 3
* Streamlit
* Pandas
* SQLAlchemy
* SQLite
* Google Gemini API

---

# 📁 Estrutura do Projeto

```text
📦 Lista-de-Compras-Inteligente
│
├── main.py
├── gen_ai.py
├── database.db
├── query_inteligente.sql
├── prompt_template.md
├── resposta_template.json
├── requirements.txt
├── .env
└── .streamlit/
    └── secrets.toml
```

### Descrição dos arquivos

| Arquivo                   | Descrição                                                              |
| ------------------------- | ---------------------------------------------------------------------- |
| `main.py`                 | Interface principal da aplicação e lógica de negócio.                  |
| `gen_ai.py`               | Comunicação com a API do Google Gemini para leitura das notas fiscais. |
| `database.db`             | Banco de dados SQLite com o histórico de compras.                      |
| `query_inteligente.sql`   | Consulta SQL responsável pelos cálculos estatísticos e recomendações.  |
| `prompt_template.md`      | Prompt utilizado para instruir o Gemini.                               |
| `resposta_template.json`  | Modelo esperado da resposta da IA.                                     |
| `requirements.txt`        | Dependências do projeto.                                               |
| `.env`                    | Chave da API do Gemini (não versionado).                               |
| `.streamlit/secrets.toml` | Configuração do OAuth do Google (não versionado).                      |

---

# ⚙️ Como executar o projeto

## 1. Clone o repositório

```bash
git clone <URL_DO_REPOSITORIO>
cd <NOME_DO_REPOSITORIO>
```

---

## 2. Crie um ambiente virtual

### Windows

```bash
python -m venv .venv

.venv\Scripts\activate
```

### Linux / macOS

```bash
python -m venv .venv

source .venv/bin/activate
```

---

## 3. Instale as dependências

```bash
pip install -r requirements.txt
```

---

## 4. Configure a API do Google Gemini

Crie um arquivo `.env` na raiz do projeto:

```env
GEMINI_API_KEY=sua_chave_aqui
```

---

## 5. Configure o Google OAuth

Crie o arquivo:

```text
.streamlit/secrets.toml
```

Conteúdo:

```toml
[auth]
redirect_uri = "http://localhost:8501/oauth2callback"
client_id = "seu_client_id_do_google_cloud.apps.googleusercontent.com"
```

---

## 6. Execute a aplicação

```bash
streamlit run main.py
```

---

# 📌 Objetivos de Aprendizagem

Este projeto foi desenvolvido para praticar:

* Desenvolvimento de aplicações web com Streamlit;
* Integração com modelos de IA Generativa;
* Processamento de imagens utilizando Google Gemini Vision;
* Manipulação e análise de dados com Pandas;
* Consultas SQL utilizando CTEs;
* Persistência de dados com SQLite e SQLAlchemy;
* Autenticação com Google OAuth 2.0;
* Organização de projetos Python.

---

# 📄 Licença

Este projeto foi desenvolvido exclusivamente para fins de estudo e aprendizado.

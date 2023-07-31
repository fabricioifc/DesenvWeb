## Mini projeto com Streamlit, Supabase e SQLite3
##### Projeto de estudo para a criação de um CRUD com Streamlit, Supabase e SQLite3

### 1. Instalar as dependências
```bash
pip install -r requirements.txt
```
### 2. Alterar as variáveis de ambiente no arquivo .streamlit/secrets.toml
```bash
cp .streamlit/secrets.toml.sample .streamlit/secrets.toml
```

### 3. Como criar o banco de dados
```bash
Abrir o arquivo src/util/sql.sql e executar os comandos no banco de dados
```

### 4. Rodar o projeto
```bash
streamlit run app.py
```
### 5. Acessar o projeto no navegador
```bash
http://localhost:8501
```
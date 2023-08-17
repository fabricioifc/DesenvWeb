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

### 3. Criar o banco de dados
```bash
python setup/create_db.py setup/seed.sql
```

### 4. Rodar o projeto
```bash
streamlit run app.py
```
### 5. Acessar o projeto no navegador
```bash
http://localhost:8501
```

### 6. Acessar o projeto em produção
```
https://desenvolvimento-web.streamlit.app/
```
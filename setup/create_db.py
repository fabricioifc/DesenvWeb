import sqlite3
import io, sys
import streamlit as st

def importar_script_sql(nome_arquivo):
    # Ler o conteúdo do arquivo SQL
    with io.open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
        conteudo_sql = arquivo.read()

    return conteudo_sql

def executar_script_sql(conexao, script_sql):
    # Criar um objeto cursor para executar comandos SQL
    cursor = conexao.cursor()

    # Executar o script SQL
    cursor.executescript(script_sql)

    # Salvar as alterações no banco de dados
    conexao.commit()

    # Fechar a conexão
    conexao.close()

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Uso: python src/util/sql.sql")
        sys.exit(1)

    arquivo_sql = sys.argv[1]
    script_sql = importar_script_sql(arquivo_sql)

    # Conectar ao banco de dados ou criar um novo se não existir
    assert st.secrets.sqlite.dbname is not None
    conexao = sqlite3.connect(st.secrets.sqlite.dbname)

    # Executar o script SQL importado
    executar_script_sql(conexao, script_sql)

    print("Database criada com sucesso!")
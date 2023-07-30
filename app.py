import streamlit as st
from src.repository.movies import MoviesRepositoryFactory
# from config import db_type

# yield will return a generator object that can be iterated over using a for loop.
def divide_chunks(l, n):
    for i in range(0, len(l), n):
        yield l[i:i + n]

def tab_movies():
    st.title("Filmes em Cartaz!")
    st.info("Clique no botão para curtir o filme!")
    st.radio("Escolha o banco de dados", ("supabase", "sqlite"), index=0, key="db_type")

    # fetch movies from database
    factory = MoviesRepositoryFactory.create()
    data = factory.get_movies()

    if len(data) == 0:
        st.warning("Não há filmes cadastrados")
        return
    
    num_movies_per_column = 3 if len(data) >= 3 else 1

    # Usando list comprehension para criar as colunas
    columns = st.columns(num_movies_per_column, gap="small")
    
    for chunk in divide_chunks(data, num_movies_per_column):
        for i, col in enumerate(columns):
            if i < len(chunk):
                movie = chunk[i]
                with col:
                    st.subheader(f"{movie.name}")
                    st.video(movie.video)
                    st.markdown(f"*{movie.sinopse}*")
                    st.markdown(f"**{movie.likes}** curtidas")
        
                    st.button("Curtir", 
                        key=movie.id, 
                        on_click=lambda movie=movie: factory.like_movie(movie), 
                        type="primary",
                    )         


def main():
    st.set_page_config(page_title="Filmes em Cartaz", page_icon="🎬", layout="wide")
    tab1, tab2 = st.tabs(["Filmes em Cartaz", "Sobre"])

    with tab1:
        tab_movies()

    with tab2:
        st.title("Sobre")
        st.markdown("Este é um projeto de exemplo para demonstrar como usar o Streamlit e o Supabase.")
        st.markdown("Para mais informações, acesse o [repositório do projeto](https://github.com/fabricioifc/DesenvWeb).")
        st.markdown("Para mais informações sobre o Streamlit, acesse o [site oficial](https://streamlit.io/).")
        st.markdown("Para mais informações sobre o Supabase, acesse o [site oficial](https://supabase.io/).")

if __name__ == "__main__":
    
    main()
import streamlit as st
from model.movie import Movie
# from config import db_type
from db.database_manager import supabase_client, sqlite_client


def get_movies():
    db_type = st.session_state.db_type

    movies = []
    if db_type == "supabase":
        db = supabase_client()
        data = db.table("movies").select("*").order("id").execute()
        for movie in data.data:
            movies.append(Movie(movie['id'],movie["name"], movie["sinopse"], movie["image"], movie["video"], movie["likes"]))
        
    elif db_type == "sqlite":
        db = sqlite_client()
        data = db.cursor().execute("SELECT id, name, sinopse, image, video, likes FROM movies ORDER BY id").fetchall()
        for movie in data:
            movies.append(Movie(movie[0],movie[1], movie[2], movie[3], movie[4], movie[5]))
        db.close()

    return movies

def like_movie(movie):
    db_type = st.session_state.db_type

    if db_type == "supabase":
        db = supabase_client()
        table = db.table("movies")
        table.update({"likes": movie.likes + 1}).eq("id", movie.id).execute()
        
    elif db_type == "sqlite":
        db = sqlite_client()
        db.cursor().execute(f"UPDATE movies SET likes = {movie.likes + 1} WHERE id = {movie.id}")
        db.commit()
        db.close()

    return True
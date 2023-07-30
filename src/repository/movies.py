import streamlit as st
from src.model.movie import Movie
# from config import db_type
from src.db.database_manager import supabase_client, sqlite_client
from abc import ABC, abstractmethod

class MoviesRepositoryFactory:
    @staticmethod
    def create():
        db_type = st.session_state.db_type
        if db_type == "supabase":
            return SupabaseMoviesRepository()
        elif db_type == "sqlite":
            return SqliteMoviesRepository()
        else:
            raise Exception("Invalid db type")

class MoviesRepository(ABC):
    @abstractmethod
    def get_movies(self):
        pass

    @abstractmethod
    def like_movie(self, movie):
        pass

class SupabaseMoviesRepository(MoviesRepository):
    def get_movies(self):
        db = supabase_client()
        data = db.table("movies").select("*").order("id").execute()
        movies = []
        for movie in data.data:
            movies.append(Movie(movie['id'],movie["name"], movie["sinopse"], movie["image"], movie["video"], movie["likes"]))
        return movies

    def like_movie(self, movie):
        db = supabase_client()
        table = db.table("movies")
        table.update({"likes": movie.likes + 1}).eq("id", movie.id).execute()
        return True
    
class SqliteMoviesRepository(MoviesRepository):
    def get_movies(self):
        db = sqlite_client()
        data = db.cursor().execute("SELECT id, name, sinopse, image, video, likes FROM movies ORDER BY id").fetchall()
        movies = []
        for movie in data:
            movies.append(Movie(movie[0],movie[1], movie[2], movie[3], movie[4], movie[5]))
        db.close()
        return movies

    def like_movie(self, movie):
        db = sqlite_client()
        db.cursor().execute(f"UPDATE movies SET likes = {movie.likes + 1} WHERE id = {movie.id}")
        db.commit()
        db.close()
        return True



# def get_movies():
#     db_type = st.session_state.db_type

#     movies = []
#     if db_type == "supabase":
#         db = supabase_client()
#         data = db.table("movies").select("*").order("id").execute()
#         for movie in data.data:
#             movies.append(Movie(movie['id'],movie["name"], movie["sinopse"], movie["image"], movie["video"], movie["likes"]))
        
#     elif db_type == "sqlite":
#         db = sqlite_client()
#         data = db.cursor().execute("SELECT id, name, sinopse, image, video, likes FROM movies ORDER BY id").fetchall()
#         for movie in data:
#             movies.append(Movie(movie[0],movie[1], movie[2], movie[3], movie[4], movie[5]))
#         db.close()

#     return movies

# def like_movie(movie):
#     db_type = st.session_state.db_type

#     if db_type == "supabase":
#         db = supabase_client()
#         table = db.table("movies")
#         table.update({"likes": movie.likes + 1}).eq("id", movie.id).execute()
        
#     elif db_type == "sqlite":
#         db = sqlite_client()
#         db.cursor().execute(f"UPDATE movies SET likes = {movie.likes + 1} WHERE id = {movie.id}")
#         db.commit()
#         db.close()

#     return True
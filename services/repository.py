from services.utils import read_file
from models.Movies import Movies

#czyta dane z pliku i konwertuje je do listy
def get_movies_data():
    data = read_file(r'C:\Users\joann\Downloads\movies.csv')
    movies = []
    for movie in data.split('\n'):
        if len(movie) and 'movieId' not in movie:
            movie = movie.split(',')
            movies.append(movie)
    return movies

def get_movies():
    #print(get_movies_data())
    return [Movies(movie[0], movie(1), movie[2]).__dict__ for movie in get_movies_data()]

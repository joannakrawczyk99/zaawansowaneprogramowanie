from models.Links import Links
from models.Ratings import Ratings
from models.Tags import Tags
from services.utils import read_file
from models.Movies import Movies


def get_movies_data():
    data = read_file(r'csv\movies.csv')
    movies = []
    for movie in data.split('\n'):
        if len(movie) and 'movieId' not in movie:
            movie = movie.split(',')
            movies.append(movie)
    return movies


def get_movies():
    # print(get_movies_data())
    return [Movies(movie[0], movie(1), movie[2]).__dict__ for movie in get_movies_data()]


def get_tags_data():
    data = read_file(r'csv\tags.csv')
    tags = []
    for tag in data.split('\n'):
        if len(tag) and 'userId' not in tag:
            tag = tag.split(',')
            tags.append(tag)
    return tags

def get_tags():
    return [Tags(tag[0], tag(1), tag[2]).__dict__ for tag in get_tags_data]


def get_ratings_data():
    data = read_file(r'csv\ratings.csv')
    ratings = []
    for rating in data.split('\n'):
        if len(rating) and 'userId' not in rating:
            rating = rating.split(',')
            ratings.append(rating)
    return ratings

def get_ratings():
    return [Ratings(rating[0], rating(1), rating[2]).__dict__ for rating in get_ratings_data()]


def get_links_data():
    data = read_file(r'csv\ratings.csv')
    links = []
    for link in data.split('\n'):
        if len(link) and 'userId' not in link:
            link = link.split(',')
            links.append(link)
    return links

def get_links():
    return [Links(link[0], link(1), link[2]).__dict__ for link in get_links_data()]
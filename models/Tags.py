from datetime import datetime

from models.Movies import Movies
from models.Ratings import Ratings


class Tags():
    def __init__(self, userId: Ratings, movieId: Movies, tag: str, timestamp: datetime):
        self.userId = userId
        self.movieId = movieId
        self.tag = tag
        self.timestamp = timestamp
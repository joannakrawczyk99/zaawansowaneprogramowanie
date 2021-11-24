from datetime import datetime

from models.Movies import Movies


class Ratings():
    def __init__(self, userId: str, movieId: Movies, rating: float, timestamp: datetime):
        self.userId = userId
        self.movieId = movieId
        self.rating = rating
        self.timestamp = timestamp

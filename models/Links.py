from models.Movies import Movies


class Links():
    def __init__(self, movieId: Movies, imdbId: str, tmdbId: str):
        self.movieId = movieId
        self.imdbId = imdbId
        self.tmdbId = tmdbId
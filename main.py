from flask import Flask
from flask_restful import Resource, Api
from services.repository import get_movies_data, get_tags_data, get_ratings_data, get_links_data

app = Flask(__name__)
api = Api(app)


class ShowMovies(Resource):
    def get(self):
        return get_movies_data()


class ShowTags(Resource):
    def get(self):
        return get_tags_data()


class ShowRatings(Resource):
    def get(self):
        return get_ratings_data()


class ShowLinks(Resource):
    def get(self):
        return get_links_data()


api.add_resource(ShowMovies, '/movies')
api.add_resource(ShowTags, '/tags')
api.add_resource(ShowRatings, '/ratings')
api.add_resource(ShowLinks, '/links')

if __name__ == '__main__':
    app.run(debug=True)

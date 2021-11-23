from flask import Flask
from flask_restful import Resource, Api
from services.repository import get_movies_data

app = Flask(__name__)
api = Api(app)


class Show(Resource):
    def get(self):
        return get_movies_data()


api.add_resource(Show, '/movies')

#utworzyć to samo wraz z endpointami dla wszystkich pliczków z classroom

if __name__ == '__main__':
    app.run(debug=True)

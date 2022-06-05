from flask import Flask, request
from flask_restful import Resource, Api
import requests

aplikacja = Flask(__name__)
api = Api(aplikacja)

class Headers(Resource):
    def get(self):

        return {'welcome': 'Witam w moim serwisie'}, 201

api.add_resource(Headers, '/')

class Alive(Resource):
    def get(self):
        return {'status': 'ok'}, 201


api.add_resource(Alive, '/hc')

class About(Resource):
    def get(self):
        return {'Application': 'Webservice',
                'Author': 'Grande Implementatore',
               'Year': '2022'}, 200


api.add_resource(About, '/about')


def start():
    if __name__ == 'Controller.Endpoints':
        aplikacja.run(debug=True)
    else:
        print(__name__)

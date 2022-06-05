from flask import Flask, request
from flask_restful import Resource, Api, reqparse
import requests

aplikacja = Flask(__name__)
api = Api(aplikacja)

class Headers(Resource):
    def get(self):
        try:
            id = request.args.get('id')
            return {'welcome': 'Witam w moim serwisie bardzo serdecznie... '+ id}, 201
        except:
            return {'error': 'Nie ma parametru'}, 400
            id == "OMG"


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

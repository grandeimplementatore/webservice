from flask import Flask
from flask_restful import Resource, Api

aplikacja = Flask(__name__)
api = Api(aplikacja)


class Alive(Resource):
    def get(self):
        return {'status': 'ok'}, 201


api.add_resource(Alive, '/hc')


def HealthCheck():
    if __name__ == 'Controller.Endpoints':
        aplikacja.run(debug=True)
    else:
        print(__name__)


class About(Resource):
    def get(self):
        return {'Application': 'Webservice',
                'Author': 'Grande'}, 200


api.add_resource(About, '/about')


def Oapce():
    if __name__ == 'Controller.Endpoints':
        aplikacja.run(debug=True)
    else:
        print(__name__)

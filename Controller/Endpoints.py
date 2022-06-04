from flask import Flask
from flask_restful import Resource, Api

aplikacja = Flask(__name__)
api = Api(aplikacja)

class Headers(Resource):
    def get(self):
        return {'welcome': 'Witam na stronie'}, 201

api.add_resource(Headers, '/')

def Headers():
    if __name__ == 'Controller.Endpoints':
        aplikacja.run(debug=True)
    else:
        print(__name__)


class Alive(Resource):
    def get(self):
        return {'status': 'ok'}, 201


api.add_resource(Alive, '/hc')


def HealthCheck():
    if __name__ == 'Controller.Endpoints':
        aplikacja.run(debug=True)
    else:
        print(__name__)


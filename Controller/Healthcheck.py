from flask import Flask
from flask_restful import Resource, Api

aplikacja = Flask(__name__)
api = Api(aplikacja)


class Alive(Resource):
    def get(self):
        return {'status': 'ok'}


api.add_resource(Alive, '/hc')


def HealthCheck():
    if __name__ == 'Controller.Healthcheck':
        aplikacja.run(debug=True)
    else:
        print(__name__)
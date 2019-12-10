# User CRUD

from flask import Blueprint
from flask_restplus import Namespace, Resource

rnd_blueprint = Blueprint('random', __name__, url_prefix='/api/random')
api_random = Namespace('random', description="random")


@api_random.route('/prueba')
class RandomREST(Resource):

    @api_random.doc('list_cats')
    def get(self):
        '''List all users'''
        return 'Hola mundo'

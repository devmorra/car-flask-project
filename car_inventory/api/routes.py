from flask import Blueprint, request, jsonify
from car_inventory.helpers import token_required
from car_inventory.models import db, User, Car, car_schema, cars_schema

api = Blueprint('api', __name__, url_prefix='/api' )

@api.route('/getdata')
@token_required
def getData(current_user_token):
    return {'some': 'value'}

@api.route('/cars', methods=['POST'])
@token_required
def createCar(current_user_token):
    make = request.json['make']
    make = request.json['make']
    make = request.json['make']
    make = request.json['make']
    make = request.json['make']
    make = request.json['make']
    car = Car()
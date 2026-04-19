from flask import Blueprint, request, jsonify
from services.battery import predict_battery
from services.range_predictor import predict_range
from services.charging import get_station

api = Blueprint('api', __name__)

@api.route('/battery', methods=['POST'])
def battery():
    data = request.json
    return jsonify(predict_battery(data))

@api.route('/range', methods=['POST'])
def range_api():
    data = request.json
    return jsonify(predict_range(data))

@api.route('/charging', methods=['GET'])
def charging():
    return jsonify(get_station())
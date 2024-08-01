from flask import Blueprint, request, jsonify

from .geocoding import find_closest_station
from .transit_service import get_transit_schedules

bp = Blueprint('routes', __name__)


@bp.route('/api/schedules', methods=['POST'])
def schedules():
    data = request.get_json()
    origin_station_id = data.get('origin_station_id')
    coordinates = data.get('coordinates')
    destination_station_id = data.get('destination_station_id')

    if coordinates:
        coordinates['latitude'] = float(coordinates.get('latitude'))
        coordinates['longitude'] = float(coordinates.get('longitude'))

    if not origin_station_id:
        origin_station_id = find_closest_station(coordinates)

    schedules = get_transit_schedules(origin_station_id, destination_station_id)
    return jsonify({"next_schedules": schedules})

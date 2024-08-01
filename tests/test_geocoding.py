from app.geocoding import find_closest_station


def test_find_closest_station():
    coordinates = {"latitude": 40.7128, "longitude": -74.0060}
    station_id = find_closest_station(coordinates)
    assert station_id == "closest_station_id"

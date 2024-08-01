import datetime


def get_transit_schedules(origin_station_id, destination_station_id):
    return [
        {
            "transit_mode": "rail",
            "eta_origin": (datetime.datetime.now() + datetime.timedelta(minutes=10)).isoformat(),
            "eta_destination": (datetime.datetime.now() + datetime.timedelta(minutes=60)).isoformat()
        },
        {
            "transit_mode": "bus",
            "eta_origin": (datetime.datetime.now() + datetime.timedelta(minutes=15)).isoformat(),
            "eta_destination": (datetime.datetime.now() + datetime.timedelta(minutes=75)).isoformat()
        }
    ]

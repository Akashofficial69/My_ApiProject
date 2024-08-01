from app.transit_service import get_transit_schedules


def test_get_transit_schedules():
    schedules = get_transit_schedules("origin_id", "destination_id")
    assert len(schedules) > 0
    assert all("transit_mode" in s for s in schedules)
    assert all("eta_origin" in s for s in schedules)
    assert all("eta_destination" in s for s in schedules)

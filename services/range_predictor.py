def predict_range(data):
    battery = data.get("battery")
    traffic = data.get("traffic")
    weather = data.get("weather")

    range_km = battery * 2

    if traffic == "high":
        range_km -= 10
    if weather == "hot":
        range_km -= 5

    return {"range_km": range_km}
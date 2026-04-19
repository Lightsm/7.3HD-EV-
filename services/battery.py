def predict_battery(data):
    battery = data.get("battery")
    temp = data.get("temperature")

    if battery > 80 and temp < 35:
        return {"status": "Good"}
    elif battery > 40:
        return {"status": "Moderate"}
    else:
        return {"status": "Poor"}
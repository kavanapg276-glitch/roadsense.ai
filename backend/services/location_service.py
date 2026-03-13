import math

# -------------------------------
# Distance Calculation
# -------------------------------

def calculate_distance(lat1, lon1, lat2, lon2):

    R = 6371  # Earth radius in km

    lat1 = math.radians(lat1)
    lon1 = math.radians(lon1)

    lat2 = math.radians(lat2)
    lon2 = math.radians(lon2)

    dlat = lat2 - lat1
    dlon = lon2 - lon1

    a = (
        math.sin(dlat / 2) ** 2 +
        math.cos(lat1) * math.cos(lat2) *
        math.sin(dlon / 2) ** 2
    )

    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    distance = R * c

    return distance


# -------------------------------
# Duplicate Detection
# -------------------------------

def is_duplicate(new_lat, new_lon, existing_locations, threshold_km=0.05):
    """
    Checks if a pothole report is near an existing one.
    Default threshold = 50 meters
    """

    for lat, lon in existing_locations:

        distance = calculate_distance(new_lat, new_lon, lat, lon)

        if distance < threshold_km:
            return True

    return False
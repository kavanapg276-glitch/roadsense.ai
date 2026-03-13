# -------------------------------
# Traffic Impact Scoring
# -------------------------------

def calculate_traffic_impact(severity: str):

    impact_map = {
        "low": "minimal",
        "medium": "moderate",
        "high": "heavy",
        "critical": "severe"
    }

    return impact_map.get(severity, "unknown")
import random

# -------------------------------
# Severity Detection (Mock AI)
# -------------------------------

def detect_severity(image_url: str):
    """
    Mock severity detection based on uploaded image.
    Later this can be replaced with Amazon Bedrock vision model.
    """

    levels = ["low", "medium", "high", "critical"]

    severity = random.choice(levels)

    confidence = round(random.uniform(0.7, 0.95), 2)

    return {
        "severity": severity,
        "confidence": confidence
    }


# -------------------------------
# Severity Explanation
# -------------------------------

def explain_severity(severity: str):

    explanations = {
        "low": "Small road damage with minimal traffic impact.",
        "medium": "Moderate pothole that may affect small vehicles.",
        "high": "Large pothole that can cause vehicle damage.",
        "critical": "Severe pothole posing accident risk and traffic disruption."
    }

    return explanations.get(severity, "Unknown severity level.")


# -------------------------------
# AI Complaint Generator
# -------------------------------

def generate_complaint(severity: str, location: str):

    complaint = f"""
Subject: Urgent pothole repair request

Location: {location}

Severity Level: {severity}

Description:
A pothole has been detected by the RoadSense AI system. 
This road damage poses a safety risk for vehicles and pedestrians.

We request the municipal authority to inspect and repair the road urgently.
"""

    return complaint.strip()


# -------------------------------
# Economic Loss Estimation
# -------------------------------

def estimate_economic_loss(severity: str):

    loss_map = {
        "low": 1000,
        "medium": 5000,
        "high": 15000,
        "critical": 50000
    }

    return loss_map.get(severity, 0)
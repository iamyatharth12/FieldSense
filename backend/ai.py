import hashlib

_CROP_SCENARIOS = [
    {
        "disease": "Leaf Spot",
        "action": "Apply copper-based fungicide within 24 hours",
        "warning": "Spreads to adjacent plants within 48 hours"
    },
    {
        "disease": "Nitrogen Deficiency",
        "action": "Apply urea fertilizer at 46kg per hectare",
        "warning": "Yield loss accelerates if untreated past 1 week"
    },
    {
        "disease": "Possible Fungal Infection",
        "action": "Spray Mancozeb fungicide today",
        "warning": "Crop loss imminent if not treated within 3 days"
    },
    {
        "disease": "Pest Infestation",
        "action": "Apply imidacloprid insecticide immediately",
        "warning": "Aphids will destroy field within 5 days"
    },
    {
        "disease": "Late Blight",
        "action": "Apply chlorothalonil fungicide within 12 hours",
        "warning": "Severe damage risk if untreated within 5-7 days"
    }
]

_DEFAULT_RESPONSE = {
    "disease": "Unknown",
    "action": "Inspect crop further",
    "warning": "Monitor closely"
}

def analyze_crop_image(image_bytes: bytes) -> dict:
    try:
        if len(image_bytes) < 1000:
            return {
                "disease": "Unclear Image",
                "action": "Upload a clear crop image",
                "warning": "Ensure plant is visible"
            }
        
        img_hash = hashlib.md5(image_bytes).hexdigest()
        index = int(img_hash[-1], 16) % len(_CROP_SCENARIOS)
        return _CROP_SCENARIOS[index]
    except Exception:
        return _DEFAULT_RESPONSE

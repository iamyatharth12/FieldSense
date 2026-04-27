import os
import requests

def get_weather_advice() -> str:
    """
    Fetches weather from Open-Meteo API and returns simple advice.
    Returns ONE short line.
    """
    try:
        url = "https://api.open-meteo.com/v1/forecast?latitude=41.6005&longitude=-93.6091&current_weather=true"
        response = requests.get(url, timeout=5)
        
        if response.status_code == 200:
            data = response.json()
            weather_code = data.get("current_weather", {}).get("weathercode", -1)
            
            # WMO Weather interpretation codes
            if (51 <= weather_code <= 67) or (80 <= weather_code <= 82) or (95 <= weather_code <= 99):
                return "Do NOT spray pesticides"
            elif weather_code in [0, 1, 2, 3]:
                return "Safe for field work (no rain expected)"
            else:
                return "Check conditions before action"
        else:
            return "Check conditions before action"
            
    except Exception as e:
        # If weather fails -> ignore silently by returning fallback
        return "Check conditions before action"

import json
import keyring
import requests
from datetime import datetime


# Hent API-nøkkelen fra nøkkelringen.
apikey = keyring.get_password("openweathermap", "api-key")

if not apikey:
    raise SystemExit("API-nøkkelen mangler i keyring.")


# Byene vi skal hente koordinater for.
cities = ["Oslo,NO", "Kongsberg,NO", "Bergen,NO"]
base_url = "https://api.openweathermap.org/geo/1.0/direct"


for city in cities:
    args = {
        "q": city,
        "limit": 1,
        "appid": apikey
    }

    response = requests.get(base_url, params=args, timeout=20)

    if response.status_code != 200:
        print(f"Kunne ikke hente {city}. HTTP-status: {response.status_code}")
        continue

    locations = json.loads(response.text)

    if not locations:
        print(f"Fant ingen koordinater for {city}.")
        continue

    location = locations[0]
    latitude = location["lat"]
    longitude = location["lon"]

    print(f"{city}: breddegrad {latitude}, lengdegrad {longitude}")

    # Bruk koordinatene fra OpenWeather i API nummer to.
    sun_url = "https://api.sunrise-sunset.org/v2"
    sun_args = {
        "lat": latitude,
        "lng": longitude,
        "date": "today"
    }

    sun_response = requests.get(sun_url, params=sun_args, timeout=20)

    if sun_response.status_code != 200:
        print(f"Kunne ikke hente soltider. HTTP-status: {sun_response.status_code}")
        continue

    sun_data = json.loads(sun_response.text)

    if not sun_data.get("sunrise") or not sun_data.get("sunset"):
        print("Ingen soloppgang eller solnedgang denne dagen.")
        continue

    sunrise = datetime.fromisoformat(sun_data["sunrise"])
    sunset = datetime.fromisoformat(sun_data["sunset"])
    daylight = sunset - sunrise

    print(f"Dato: {sunrise.date()}")
    print(f"Soloppgang: {sunrise.strftime('%H:%M:%S')}")
    print(f"Solnedgang: {sunset.strftime('%H:%M:%S')}")
    print(f"Tidssone: {sun_data['tzid']}")
    print(f"Dagens lengde: {daylight}")
    print("Soldata: https://sunrise-sunset.org\n")    
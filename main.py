import keyring
import requests
from sun_api import SunApi
from datetime import datetime
from geo_api import GeoApi


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

    try:
        locations = GeoApi().fetch(base_url, args)
    except requests.RequestException:
        print(f"Kunne ikke hente koordinater for {city}.")
        continue

    if not locations:
        print(f"Fant ingen koordinater for {city}.")
        continue

    location = locations[0]
    latitude = location.lat
    longitude = location.lon

    print(f"{city}: breddegrad {latitude}, lengdegrad {longitude}")

    # Bruk koordinatene fra OpenWeather i API nummer to.
    sun_url = "https://api.sunrise-sunset.org/v2"
    sun_args = {
        "lat": latitude,
        "lng": longitude,
        "date": "today"
    }

    try:
        sol = SunApi().fetch(sun_url, sun_args)
    except (requests.RequestException, KeyError):
        print(f"Kunne ikke hente soltider for {city}.")
        continue

    if not sol.sunrise or not sol.sunset:
        print("Ingen soloppgang eller solnedgang denne dagen.")
        continue

    sunrise = datetime.fromisoformat(sol.sunrise)
    sunset = datetime.fromisoformat(sol.sunset)

    daylight = sunset - sunrise

    print(f"Dato: {sunrise.date()}")
    print(f"Soloppgang: {sunrise.strftime('%H:%M:%S')}")
    print(f"Solnedgang: {sunset.strftime('%H:%M:%S')}")
    print(f"Tidssone: {sol.timezone}")
    print(f"Dagens lengde: {daylight}")
    print("Soldata: https://sunrise-sunset.org\n")    
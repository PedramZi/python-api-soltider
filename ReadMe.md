# Soltider med Python og API-er

## Hva programmet gjør

Programmet henter koordinater og dagens soltider for Oslo, Kongsberg
og Bergen. Det viser breddegrad, lengdegrad, dato, soloppgang,
solnedgang, tidssone og dagens lengde i terminalen.

Programmet bruker to API-kilder:

1. OpenWeather Geocoding API henter koordinater fra bynavn.
   Dette API-et krever en personlig API-nøkkel.
2. Sunrise-Sunset API bruker koordinatene fra OpenWeather til å
   hente soloppgang og solnedgang. Dette API-et krever ingen nøkkel.

API-nøkkelen lagres med Python keyring og hentes ved kjøring.
Den ligger ikke i kildekoden.

### NB! Nøkkelen følger ikke med når prosjektet lastes ned fra GitHub.

## Instruksjonene nedenfor gjelder Windows. 
Åpne en terminal i prosjektmappen før du kjører kommandoene.

## Opprett et virtuelt miljø

py -m venv .venv


Kommandoen oppretter et eget Python-miljø i mappen .venv

## Installer pakkene

.\.venv\Scripts\python.exe -m pip install -r requirements.txt


Kommandoen installerer pakkene som står i requirements.txt.

## NB! Skaff og lagre egen API-nøkkel

Opprett en konto på https://home.openweathermap.org/users/sign_up,
bekreft epostadressen og finn nøkkelen under API keys.

Lagre nøkkelen på din egen PC:

.\.venv\Scripts\python.exe -m keyring set openweathermap api-key


Lim inn API-nøkkelen

## Kjør programmet

.\.venv\Scripts\python.exe main.py

Programmet skriver resultatene for de tre byene til terminalen.
Soltidene vises i tidssonen som returneres av Sunrise-Sunset.

![Resultat](Resultat.png)

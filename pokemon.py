import requests
import sys

if len(sys.argv) < 2:
    sys.exit("Too few arguments")

try:
    response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{sys.argv[1]}")
    response.raise_for_status()
except requests.HTTPError:
    sys.exit("Couldn't complete the request")

abilities = response.json()

for ability in abilities["abilities"]:
    print(f"* {ability['ability']['name']}")

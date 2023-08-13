import json
from unicodedata import name
import requests
from pprint import PrettyPrinter

pp = PrettyPrinter()
url = ("https://pokeapi.co/api/v2/ability/1/")
params = {
    name:"garbodor"
}

def main():
    r = requests.get(url)
    status = r.status_code
    if status != 200:
        quit()
    else:
        get_pokedex(status)

def get_pokedex(x):
    print("status code: ", + x)
    response = requests.get(url,params=params).json()
    pp.pprint(response)

main()
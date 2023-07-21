from requests import request
import json

def get_arab_countries():
    arab_countries_json = request('get','https://restcountries.com/v3.1/lang/ara').content
    arab_countries = json.loads(arab_countries_json)
    for country in arab_countries:
        print(country['name']['common'])

def main():
    get_arab_countries()

main()
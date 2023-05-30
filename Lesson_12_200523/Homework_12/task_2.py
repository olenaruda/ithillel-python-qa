import requests
import json


def fetch_data(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None


def get_homeworld_info(url):
    homeworld_data = fetch_data(url)
    if homeworld_data:
        homeworld_info = {
            'name': homeworld_data['name'],
            'climate': homeworld_data['climate'],
            'terrain': homeworld_data['terrain'],
            'population': homeworld_data['population'],
            'url': url
        }
        return homeworld_info
    else:
        return None


def get_pilots_info(pilots):
    pilots_info = []
    for pilot_url in pilots:
        pilot_data = fetch_data(pilot_url)
        if pilot_data:
            homeworld_info = get_homeworld_info(pilot_data['homeworld'])
            pilot_info = {
                'name': pilot_data['name'],
                'height': pilot_data['height'],
                'mass': pilot_data['mass'],
                'homeworld': homeworld_info
            }
            pilots_info.append(pilot_info)
    return pilots_info


def get_millennium_falcon_info():
    starship_url = 'https://swapi.dev/api/starships/?search=Millennium%20Falcon'
    starship_data = fetch_data(starship_url)
    if starship_data and starship_data['results']:
        starship_info = starship_data['results'][0]
        pilots_info = get_pilots_info(starship_info['pilots'])
        return {
            'name': starship_info['name'],
            'max_speed': starship_info['max_atmosphering_speed'],
            'class': starship_info['starship_class'],
            'pilots': pilots_info
        }
    else:
        return None


def main():
    millennium_falcon_info = get_millennium_falcon_info()
    if millennium_falcon_info:
        print('Information about Millennium Falcon:')
        print('Name:', millennium_falcon_info['name'])
        print('Maximum Speed:', millennium_falcon_info['max_speed'])
        print('Class:', millennium_falcon_info['class'])
        print('Pilots:')
        for pilot in millennium_falcon_info['pilots']:
            print('  Name:', pilot['name'])
            print('  Height:', pilot['height'])
            print('  Mass:', pilot['mass'])
            print('  Homeworld:', pilot['homeworld']['name'])
            print('  Homeworld Climate:', pilot['homeworld']['climate'])
            print('  Homeworld Terrain:', pilot['homeworld']['terrain'])
            print('  Homeworld Population:', pilot['homeworld']['population'])
            print('  Homeworld URL:', pilot['homeworld']['url'])
            print()

            with open('millennium_falcon_info.json', 'w') as file:
                json.dump(millennium_falcon_info, file)
            print('Millennium Falcon information saved to millennium_falcon_info.json')
        else:
            print('Failed to retrieve Millennium Falcon information')


if __name__ == '__main__':
    main()


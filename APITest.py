import requests


def list_character_names():
    # url = 'https://swapi.dev/api/people/1'
    url = "https://swapi.dev/api/people/?page=1"
    r = requests.get(url)
    d1 = r.json()
    print("Total characters = " + str(d1['count']))
    length = len(d1['results'])

    for i in range(length):
        print(d1['results'][i]['name'], "  ", d1['results'][i]['films'][0])

    while d1['next'] is not None:
        print("NEXT page " + str(d1['next']))
        r = requests.get(d1['next'])
        d1 = r.json()
        length = len(d1['results'])
        for i in range(length):
            print(d1['results'][i]['name'], "  ", d1['results'][i]['films'][0])


def search_character_or_planet(name, type):
    url = "https://swapi.dev/api/people/?page=1"
    if type == "planets":
        url = url.replace('people', 'planets')
    r = requests.get(url)

    while True:
        if r.status_code == 200:
            d1 = r.json()
            length = len(d1['results'])

            for i in range(length):
                if d1['results'][i]['name'] == name:
                    for key, value in d1['results'][i].items():
                        print("{} : {}".format(key, value))
                    return

            r = requests.get(d1['next'])

        else:
            print("Resource not found.")
            break


search_character_or_planet('Ojom', 'planets')
#search_character_or_planet('Boba Fett', 'people')
# list_character_names()

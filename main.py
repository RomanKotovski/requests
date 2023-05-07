import requests

def superhero():
    url = "https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/all.json"
    response = requests.get(url=url)
    all_hero = response.json()
    hero_name = ['Hulk', 'Captain America', 'Thanos', 'Iron Man', 'Thor']
    intellegence_hero = {}
    for hero in all_hero:
        if hero['name'] in hero_name:
            intellegence_hero[hero['name']] = hero['powerstats']['intelligence']
    print(intellegence_hero.items())

if __name__ == '__main__':
    superhero()

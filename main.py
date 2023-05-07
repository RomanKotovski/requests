import requests
import operator

def superhero():
    url = "https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/all.json"
    response = requests.get(url=url)
    all_hero = response.json()
    hero_name = ['Hulk', 'Captain America', 'Thanos']
    intellegence_hero = {}
    for hero in all_hero:
        if hero['name'] in hero_name:
            intellegence_hero[hero['name']] = hero['powerstats']['intelligence']
    print(max(intellegence_hero.items(), key=operator.itemgetter(1)))

if __name__ == '__main__':
    superhero()


###############################################################################

from pprint import pprint
import requests

class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': f'OAuth {self.token}'
        }
    def get_files_list(self):
        files_url = 'https://cloud-api.yandex.net/v1/disk/resources/files'
        headers = self.get_headers()
        responce = requests.get(files_url, headers=headers)
        return responce.json()

    def upload_link(self, disk_file_path):
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = self.get_headers()
        params = {"path": disk_file_path, "overwrite": "true"}
        responce = requests.get(upload_url, headers=headers, params=params)
        pprint(responce.json())
        return responce.json()
    def upload_file_to_disk(self, disk_file_path, filename):
        href = self.upload_link(disk_file_path=disk_file_path).get("href", "")
        responce = requests.put(href, data=open(filename, 'rb'))
        if responce.status_code == 201:
            print("Success")

if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    filename = "\README.md"
    token = 'y0_AgAAAAAzTKoOAADLWwAAAADirnYaBAZfFooQRhSQlYuCtLWT-UTLq6U'
    uploader = YaUploader(token)
    result = uploader.upload_file_to_disk(filename)
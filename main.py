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


class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': f'OAuth {self.token}'
        }
    def upload_link(self, disk_file_path):
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = self.get_headers()
        params = {"path": disk_file_path, "overwrite": "true"}
        responce = requests.get(upload_url, headers=headers, params=params)
        return responce.json()
    def upload_file_to_disk(self, disk_file_path, filename):
        href = self.upload_link(disk_file_path=disk_file_path).get("href", "")
        responce = requests.put(href, data=open(filename, 'rb'))
        if responce.status_code == 201:
            print("Файл загружен!")

if __name__ == '__main__':
    filename = 'KungFuKitty111.jpg'  #название файла на я.диске
    token = ''   #токен
    disk_file_path = "C:\\Users\\Roma\\OneDrive\\Рабочий стол\\Homework\\requests\\KungFuKitty.jpg"  #путь к файлу на пк
    result = YaUploader(token).upload_file_to_disk(filename, disk_file_path)
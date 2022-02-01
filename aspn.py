import sys
from io import BytesIO
# Этот класс поможет нам сделать картинку из потока байт
from AWEB import spn
import requests
from PIL import Image

# Пусть наше приложение предполагает запуск:
# python search.py Москва, ул. Ак. Королева, 12
# Тогда запрос к геокодеру формируется следующим образом:
toponym_to_find = " ".join(sys.argv[1:])
geocoder_api_server = "http://geocode-maps.yandex.ru/1.x/"

geocoder_params = {
    "apikey": "40d1649f-0493-4b70-98ba-98533de7710b",
    "geocode": toponym_to_find,
    "format": "json"}

response = requests.get(geocoder_api_server, params=geocoder_params)

if not response:
    # обработка ошибочной ситуации
    pass

# Преобразуем ответ в json-объект
json_response = response.json()
# Получаем первый топоним из ответа геокодера.
toponym = response.json()["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]
# Координаты центра топонима:
ll = toponym["Point"]["pos"]
# Долгота и широта:
toponym_longitude, toponym_lattitude = ll.split(" ")

deltaLongtitude, deltaLatitude = spn(toponym)
map_params = {
    "ll": ",".join([toponym_longitude, toponym_lattitude]),
    "spn": ",".join(str(i) for i in [deltaLongtitude, deltaLatitude]),
    "l": "map", "pt": ",".join([toponym_longitude, toponym_lattitude])
}
response = requests.get("http://geocode-maps.yandex.ru/1.x/", params=geocoder_params)
Image.open(BytesIO(response.content)).show()

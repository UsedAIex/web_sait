import sys
import requests
xy = ''
xy += '9'
xy += ','
xy += '1'
print(str(xy))
url = "http://static-maps.yandex.ru/1.x"
params = {
    "ll": '37.46359,54.673317',
    "spn": "0.003,0.003",
    "l": "map"
}
response = requests.get(url, params=params)

if not response:
    print("Ошибка выполнения запроса:")
    print("Http статус:", response.status_code, "(", response.reason, ")")
    sys.exit(1)

# Запишем полученное изображение в файл.
map_file = "static/map.png"
with open(map_file, "wb") as file:
    file.write(response.content)
print(map_file)
# Инициализируем pygame

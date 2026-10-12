import json     # импорт для работы с json 

with open("users.json", "r", encoding="utf-8") as f:
    users = json.load(f)        # чтение файла
    
cities = {}             # пустой словарь
for user in users:      # обработка по условию задачи
    city = user["address"]["city"]
    name = user["name"]
    if city not in cities:      # проверка, есть ли ключ города в словаре и если нет - добавление его туда с пустым значением
        cities[city] = []
    cities[city].append(name)
    
with open("cities.json", "w", encoding="utf-8") as f:   # запись в файл
    json.dump(cities, f, ensure_ascii=False, indent=2)
    
#print(cities)

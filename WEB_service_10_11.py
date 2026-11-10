'''HTTP-
GET
POST
PUT
DELETE

Коды ответов веб-сервера:
500 - Internal Server Error - внутренняя ошибка сервера
503 - Service Anivalible - сервис недоступен
404 - не найдено
405 - 
429 - Too Many Request - слишком много запросов
400 - Bad Request
302 - Найдено
301 - Перемещено
200 - Успешно'''
#----------------------------------------------------------------------------

import requests
'''
response = requests.get('https://jsonplaceholder.typicode.com/posts/7')
print(f"Статус код: {response.status_code}")
print(f"Текст ответа: {response.text}")
data = response.json()
print(f"Заголовок поста: {data['title']}")
payload = {'user':'ivan', 'age':25}
response = requests.get('https://httpbin.org/get', params=payload)
print(response.url)
print(response.text)'''
#-----------------------------------------------------------------------------
'''
url = 'https://httpbin.org/post'
payload_json={'title':'foo', 'body':'bar', 'userID':7}
response1 = requests.post(url, json=payload_json)
print(response1.text)'''
#-----------------------------------------------------------------------------
'''
url = 'https://httpbin.org/post'
payload_form = {'username':'admin', 'password':'secret'}
response2 = requests.post(url, data=payload_form)
print(response2.text)'''
'''
headerz = {
    'User-Agent':'MyAwesomeUserAgent/1.0',
    'Authorization':'Bearer *******' # Bearer - один из видов авторизационных токенов, видя которые, сервер пропускает тех, кто заходит
    }
response = requests.get('https://api.github.com/user', headers = headerz)
print(response.text)
#print(response.headers)
# ДЗ: метод requests.Sessions

try:
    response = request.get('url', timeout=5)
    response.raise_for_status()
except request.exceptions.Timeout:
    print('Сервер залип, время вышло')
except request.exceptions.HTTPError as e:
    print(f'Ошибка http {e}')
except request.exceptions.ConnectionError:
    print('Нет связи с сервером')
except request.exceptions.RequestException as e:
    print (f'Непредвиденная ошибка {e}')
    
url = 'http://site.com/downloads/large_movie.mp4'
with requests.get(url, stream=True) as r:
    r.raise_for_status()
    with open('vidos.mp4', 'wb') as f:
        for chunk in r.iter_content(chunk_size=8192):
            f.write(chunk)'''
            
            
# Асинхронные библиотеки: aiohttp, httpx
url_name = 'https://api.agify.io?name=Фёдор'
url_pol = 'https://api.genderize.io?name=Фёдор'

try:
    response1 = requests.get(url_name, timeout=5)
    response1.raise_for_status()
    data1 = response1.json()        
    age = data1["age"]             
    response2 = requests.get(url_pol, timeout=5)
    response2.raise_for_status()
    data2 = response2.json()        
    probability = data2["probability"]
    
    print(f"Цель: Фёдор. Вероятный возраст: {age}")
    print(f"Вероятность женского пола: {probability}%")
    
except requests.exceptions.Timeout:
    print('Сервер залип, время вышло')
except requests.exceptions.HTTPError as e:
    print(f'Ошибка http {e}')
except requests.exceptions.ConnectionError:
    print('Нет связи с сервером')
except requests.exceptions.RequestException as e:
    print (f'Непредвиденная ошибка {e}')
    


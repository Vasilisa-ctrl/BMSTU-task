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
#print(response.headers)'''
# ДЗ: метод requests.Sessions
'''
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
url_active = 'https://jsonplaceholder.typicode.com/posts'
url_server = 'https://httpbin.org/post'
url_pic = 'https://picsum.photos/400/300'

try:
    # Этап 1
    responseAge = requests.get(url_name, timeout=5)
    responseAge.raise_for_status()
    dataAge = responseAge.json()        
    age = dataAge["age"]             
    responsePol = requests.get(url_pol, timeout=5)
    responsePol.raise_for_status()
    dataPol = responsePol.json() 
    pol = dataPol["gender"]       
    probability = dataVer["probability"]
    
    print(f"Цель: Фёдор. Вероятный возраст: {age}")
    print(f"Вероятность женского пола: {probability}%")
    
    # Этап 2
    ID = {'userId': 7}
    headerBrowse = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) СекретныйАгентБот/1.0',
    'Accept-Language':'ru-RU,ru;q=0.9'
    }
    
    responseActive = requests.get(url_active, params=ID, timeout=5)
    responseActive.raise_for_status()
    data = responseActive.json()       
    wc = len(responseActive.text) 
    print(wc)
    print(responseActive.headers)    
    
    # Этап 3
    ResultData = {'name': 'Фёдор', 'age': age, 'gender': pol, 'number_of_rows': wc}
    responseResult = requests.post(url_server, json=ResultData, timeout=5)
    answer = (responseResult.text)
    print(answer)
    
    # Этап 4
    with requests.get(url_pic, stream=True) as r:
        r.raise_for_status()
        with open('evidence.jpg', 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)
        print(len(r.content))
    # Этап 5
    responseExample1 = ('https://httpbin.org/status/404', timeout=5)
    responseExample2 = ('https://httpbin.org/delay/6', timeout=3)
    
    
except requests.exceptions.Timeout:
    print('Сервер залип, время вышло. Приносим извинения, скоро должно заработать!')
except requests.exceptions.HTTPError as e:
    print(f'Ошибка http {e}. Извините, мы уже работаем над неисправностью!')
'''except requests.exceptions.ConnectionError:
    print('Нет связи с сервером')
except requests.exceptions.RequestException as e:
    print (f'Непредвиденная ошибка {e}')'''
    


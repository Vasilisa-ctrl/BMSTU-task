import requests

url_name = 'https://api.agify.io?name=Фёдор'
url_pol = 'https://api.genderize.io?name=Фёдор'
url_active = 'https://jsonplaceholder.typicode.com/posts'
url_server = 'https://httpbin.org/post'
#url_pic = 'https://picsum.photos/400/300' ???
url_pic = 'https://httpbin.org/image/jpeg'

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
    probability = dataPol["probability"]*100
    
    print(f"Цель: Фёдор. Вероятный возраст: {age}")
    print(f"Вероятность женского пола: {probability}%")
    
    # Этап 2
    userId={'userId': 7}
    headersBrowse = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) SecretAgentBot/1.0',
    'Accept-Language': 'ru-RU,ru;q=0.9'
    }
    
    responseActive = requests.get(url_active, params=userId, headers=headersBrowse, timeout=5)
    responseActive.raise_for_status()
    data = responseActive.json() 
    wc = len(data)       
    print(f'Количество полученных постов: {wc}')
    print(f'Заголовок первого поста: {data[0]['title']}')    
    
    # Этап 3
    ResultData = {'name': 'Фёдор', 'age': age, 'gender': pol, 'number_of_rows': wc}
    responseResult = requests.post(url_server, json=ResultData, timeout=5)
    responseResult.raise_for_status()
    DataAnswer = responseResult.json()
    answer = DataAnswer["json"]
    print(f'Данные, записанные в поле json: {answer}')
    
    # Этап 4
    with requests.get(url_pic, stream=True) as r:
        r.raise_for_status()
        with open('evidence.jpg', 'wb') as f:
            f.write(r.content)
        print(f'Размер скачанного файла: {len(r.content)} B')
        
except requests.exceptions.Timeout:
    print('Сервер залип, время вышло. Приносим извинения, скоро должно заработать!')
except requests.exceptions.HTTPError as e:
    print(f'Ошибка http {e}. Извините, мы уже работаем над неисправностью!')  

    # Этап 5
try:
    responseExample1 = requests.get('https://httpbin.org/status/404', timeout=5)
    responseExample1.raise_for_status()
except requests.exceptions.Timeout:
    print(f'Сервер {"https://httpbin.org/status/404"} залип, время вышло. Приносим извинения, скоро должно заработать!')
except requests.exceptions.HTTPError as e:
    print(f'Ошибка http {e}. Извините, мы уже работаем над неисправностью!')
    
try:    
    responseExample2 = requests.get('https://httpbin.org/delay/6', timeout=3)
    responseExample2.raise_for_status()
except requests.exceptions.Timeout:
    print(f'Сервер {"https://httpbin.org/delay/6"} залип, время вышло. Приносим извинения, скоро должно заработать!')
except requests.exceptions.HTTPError as e:
    print(f'Ошибка http {e}. Извините, мы уже работаем над неисправностью!')  
    
 
    
'''except requests.exceptions.ConnectionError:
    print('Нет связи с сервером')
except requests.exceptions.RequestException as e:
    print (f'Непредвиденная ошибка {e}')'''

# CGI - Common Gateway Interface
# ДЗ nginx - история создания

# FastCGI/mod_python
# WSGI - Web Server Gateway Interface
# ASGI - Asynchronous Server Gateway Interface
'''
def app(environ, start_response):
    status='200 OK'
    headers=[
        ('Content-Type', 'text/plain; charset=utf-8'),
        ]
    start_response(status, headers)
    return [b'hello, world']

from wsgiref.simple_server import make_server

with make_server('', 8000, app) as httpd:
    print('Сервер запущен на http://localhost:8000')
    httpd.serve_forever()'''

#------------------------------------------------------  
'''  
from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello():
    return 'Hello, world!'
if __name__=='__main__':
    app.run()
    
# MVC - Model View Controller 
# Прочитать про Django, Gunicorn, uWSGI
# Прочитать про проблему c10k
'''
#--------------------------------------------------------
'''
from flask import Flask, request, jsonify
import time
import random

app = Flask(__name__)
@app.route('/')
def index():
    return '<h1>Привет от синхронного сервера!</h1>'
    
@app.route('/api/data')
def get_data():
    time.sleep(2)
    return jsonify({
    'message':'Данные получены',
    'value': random.randint(1, 100)
    })
    
@app.route('/api/echo', methods=['POST'])
def echo():
    data = request.get_json(force=True)
    return jsonify({'receive':data})
    
if __name__==('__main__'):
    app.run(debug=True, port=5000)
'''
#------------------------------------------------------------
'''    
result = db.query('Долгий SQL-запрос')
result = await db.query('Долгий SQL')
EventLoop (один поток)
задача А: запрос к БД - await
задача Б: запрос к API - await
задача В: чтение файла - await
 |
задача А: данные пришли - возврат из await
 |
задача Б: данные пришли - возврат из await
'''

# ДЗ - прочитать про "состояние гонки"
'''
import asyncio
async def task(name, delay):
    print(f'[{name}] начал работу')
    await asyncio.sleep(delay)
    print(f'[{name}] закончил работу')
async def main():
    await asyncio.gather(
    task("A", 2),
    task("B", 1),
    task("C", 5)
    )
asyncio.run(main())
'''
'''
- Uvicorn
- Hypercorn
- Daphna
'''
# FastAPI
from fastapi import FastAPI
app = FastAPI()
@app.get('/')
async def root():
    return {'message':'Hello, world!'}

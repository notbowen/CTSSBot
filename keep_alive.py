# keep_alive.py
# To host the bot
# Author: wHo#6933

from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def home():
    return 'bonjour'

def run():
  app.run(host='0.0.0.0',port=8080)

def keep_alive():  
    t = Thread(target=run)
    t.start()
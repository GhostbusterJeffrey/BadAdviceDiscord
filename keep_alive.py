from flask import Flask
from threading import Thread
from random import randint

app = Flask('')

quotes = ["If you have to try, ||dont.||", "If you cant tell the difference between good and bad advice, ||you don't need advice.||", "When in conflict, ||just walk away.||", "When in doubt, ||ask someone else, not me, I can't help.||", "If life is a soup, ||then I am a fork.||"]

@app.route('/')
def home():
    return "Hello, I am alive!"

@app.route('/api')
def badadvice():
    return "{\"advice\": \"" + quotes[randint(0, len(quotes) - 1)] + "\"}"

def run ():
  app.run(host='0.0.0.0',port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()
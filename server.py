from flask import Flask, render_template
from threading import Thread

app = Flask(__name__)

@app.route('/')
def home():
  return render_template("index.html")

def run():
  app.run()

def runserver():
  thd = Thread(target=run)
  thd.start()
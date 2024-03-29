from flask import Flask, redirect
import random
import requests

app = Flask(__name__)

def getRandomProject():
    try:
        running = True
        notfoundtext = "{\"code\":\"NotFound\",\"message\":\"\"}"
        projectcount = 908838871
        while running:
            idrandom = random.randint(0,projectcount)
            urlrandom = f"https://api.scratch.mit.edu/projects/{idrandom}"
            if requests.get(urlrandom).text != notfoundtext:
                running = False
                return str(idrandom)
    except Exception:
        return 0

@app.route('/')
def home():
    return redirect(f"https://scratch.mit.edu/projects/{getRandomProject()}", code=200)

@app.route('/v1/api')
def ok():
    return getRandomProject()

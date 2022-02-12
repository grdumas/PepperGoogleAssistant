# disclaimer: code does not currently function, this is a draft for dev purposes

from flask import Flask

app = Flask(__name__)

app.route('/pepper')
def pepper_client():
    # connect with the Pepper robot

def record_begin():
    # begin recording audio on the Pepper

def play_assistant():
    # play the Google Assistant's respose via Pepper's speakers

app.route('/google')
def gconnect():
    # connect with the google api


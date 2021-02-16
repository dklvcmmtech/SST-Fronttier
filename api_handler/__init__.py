from flask import Flask, render_template, request
import os
from flask import jsonify
import requests
app = Flask(__name__)

url_endpoint = 'http://main:5000/readevents'

@app.route("/")
def hello():
    return render_template('index.html')


@app.route("/events",methods=['GET'])
def getEvents():
    print("GETEVENTS")
    params1 = {
        'sDateTime':request.args['startTime'],
        'eDateTime':request.args['endTime']
    }
    #validate_Function()
    #ret_obj = {'return':'GET'}
    print("output::---------------------------------------->>>>>>>>>>>>>",params1)
    content = requests.get(url=url_endpoint, params = params1)
    print(str(content.json()))
    return str(content.json())
    #return "Thanks"


@app.route("/events",methods=['POST'])
def postEvents():
    print("POSTEVENTS")
    #validate_function()
    ret_obj = {'return':'POST'}
    return jsonify(ret_obj)
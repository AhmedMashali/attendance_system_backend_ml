from flask import request
from flask import Blueprint
from utils import *
import json


views = Blueprint(__name__, "views")

@views.route("/")
def index():
    return "Flask Server!"


# handle post request that is sent from Node.js app
@views.route('/postdata', methods = ['POST']) 
def postdata():
    # extract json data from the request
    data = request.get_json()
    # print(data) 
    # do something with this data variable that contains the data from the node server

    decode64_and_save_img("img/test_image_6.jpg", data)

    return_image = open_and_encode64("img/ahmed_mohamed.jpg")

    # return data to Node.js app
    return json.dumps({"newdata":f"{return_image}"})
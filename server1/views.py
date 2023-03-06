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

    decode64_and_save_img("img/class/test_image_6.jpg", data["class_img"])

    for key in data["faces"]:
        value = data["faces"][key]
        decode64_and_save_img(f"img/faces/{key}.jpg", value)

    # print(data) 
    # do something with this data variable that contains the data from the node server


    return_image = open_and_encode64("img/ahmed_mohamed.jpg")

    # return data to Node.js app
    return json.dumps({"newdata":f"{return_image}"})

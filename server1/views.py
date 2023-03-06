from flask import request
from flask import Blueprint
from utils import *
from recognition import *
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
    save_faces(data)
    attendance = recognition()
    # print(attendance)

    # do something with this data variable that contains the data from the node server


    # return_image = open_and_encode64("img/ahmed_mohamed.jpg")

    # return data to Node.js app
    print('is here!')
    return json.dumps(attendance)

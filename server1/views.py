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

    # decoding base64 taken image and saving it in taken img folder
    decode64_and_save_img("img/taken img/image.jpg", data["taken_img"])

    # decoding reference faces and saving it in faces folder
    save_faces(data)

    # getting attendance
    attendance = recognition()

    # clear folders from images
    clear_folder('img/taken img')
    clear_folder('img/faces')


    # return attendace as JSON
    return json.dumps(attendance)

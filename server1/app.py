from flask import Flask, request 
import json
import base64


app = Flask(__name__) 
    
@app.route('/')
def index(): 
    return 'flask server'

# handle post request that is sent from Node.js app
@app.route('/postdata', methods = ['POST']) 
def postdata():
    # extract json data from the request
    data = request.get_json()
    # print(data) 
    # do something with this data variable that contains the data from the node server

    decode64_and_save_img("img/test_image_6.jpg", data)

    return_image = open_and_encode64("img/ahmed_mohamed.jpg")

    # return data to Node.js app
    return json.dumps({"newdata":f"{return_image}"})



def decode64_and_save_img(path, data):
    with open(path, "wb") as fh:
        fh.write(base64.b64decode(data))

def open_and_encode64(path):
    with open(path, "rb") as image_file:
        return base64.b64encode(image_file.read())
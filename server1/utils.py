import base64

def decode64_and_save_img(path, data):
    with open(path, "wb") as fh:
        fh.write(base64.b64decode(data))

def open_and_encode64(path):
    with open(path, "rb") as image_file:
        return base64.b64encode(image_file.read())
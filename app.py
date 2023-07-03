from flask import Flask
from views import views
from recognition import prepare_refernce_faces

prepare_refernce_faces()

app = Flask(__name__)
app.register_blueprint(views, url_prefix="/")


if __name__ == "__main__":
    app.run(debug=True, port=5000)

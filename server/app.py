from flask import Flask, request
from main import main;

app = Flask(__name__)

@app.route('/', methods = ["GET","POST"])
def index():
    if request.method == "GET":
        pass
    else:
        parameters = request.form;
        main(parameters);


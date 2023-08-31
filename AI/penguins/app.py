from flask import Flask, request, jsonify, render_template
import pickle
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder
from sklearn import tree

import warnings
warnings.warn = lambda *args, **kwargs: 1+1

app = Flask(__name__)

with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

@app.route('/')
def hello_world():
    print(request.remote_addr)
    return render_template("template.html")

@app.route("/submit", methods=["POST"])
def submit():
    if request.remote_addr == "10.128.130.251":
        return jsonify({"status": "error", "value": "Blocked IP"})

    data = np.array([request.json["data"]])
    print(data)

    prediction = model.predict(data)[0]
    prediction = [
        "Adelie Penguin (Pygoscelis adeliae)", 
        "Gentoo penguin (Pygoscelis papua)", 
        "Chinstrap penguin (Pygoscelis antarctica)"
    ][int(prediction)]

    print(prediction)

    return jsonify({"status":"success", "value": prediction})

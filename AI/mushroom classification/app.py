from flask import Flask, request, jsonify, render_template, redirect, url_for
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

@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        print(request.form)

        arr = []
        for i in request.form.items():
            arr.append(i[1])

        print(arr)
        prediction = model.predict(np.array(arr).reshape(1, -1))[0]

    try:
        prediction = ["Safe to eat", "Poisnus"][round(float(prediction))]
    except KeyError:
        prediction = None
    except UnboundLocalError:
        prediction = None

    return render_template("template.html", prediction=prediction)


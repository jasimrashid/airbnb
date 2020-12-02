from flask import Blueprint, request, jsonify, render_template
import os
from sklearn.linear_model import LogisticRegression
import pandas as pd
import pickle
import traceback


MODEL_FILEPATH = os.path.join(os.path.dirname(
    __file__), "..", "models", "latest_model.pkl")


stats_routes = Blueprint("stats_routes", __name__)

# LOAD SERIALIZED MODEL

# def load_model():
#     print("LOADING THE MODEL...")
#     with open(MODEL_FILEPATH, "rb") as model_file:
#         saved_model = pickle.load(model_file)
#     return saved_model

# retired: route from build week
# @stats_routes.route("/predict", methods=["GET"])
# def predict_json():

# ROUTE FOR RUNNING APP THROUGH BROWSWER REQUEST
# @stats_routes.route("/predict_form", methods=["POST"])
# def predict_html():


@stats_routes.route("/predict", methods=["POST"])
def predict():
    print("PREDICT ROUTE...")
    print("FORM DATA:", dict(request.form))
    # > {'screen_name_a': 'elonmusk', 'screen_name_b': 's2t2', 'tweet_text': 'Example tweet text here'}
    screen_name_a = request.form["screen_name_a"]
    screen_name_b = request.form["screen_name_b"]
    tweet_text = request.form["tweet_text"]

    print("-----------------")
    print("FETCHING TWEETS FROM THE DATABASE...")

    # TODO

    print("-----------------")
    print("TRAINING THE MODEL...")

    classifier = LogisticRegression()
    # TODO: classifier.fit(___________, ___________)

    print("-----------------")
    print("MAKING A PREDICTION...")

    # TODO

    return render_template("prediction_results.html",
                           screen_name_a=screen_name_a,
                           screen_name_b=screen_name_b,
                           tweet_text=tweet_text,
                           screen_name_most_likely="TODO"
                           )

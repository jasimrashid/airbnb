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


def load_model():
    print("LOADING THE MODEL...")
    with open(MODEL_FILEPATH, "rb") as model_file:
        saved_model = pickle.load(model_file)
    return saved_model


@stats_routes.route("/predict", methods=["GET"])
def predict_json():
    lr = load_model()
    print("CLASSIFIER:", lr)
    print('Model loaded')

    # try:
    #     json_ = request.json
    #     print(json_)

    #     query = pd.DataFrame(json_)
    #     query = query[['a', 'b']]

    #     prediction = list(lr.predict(query))

    #     return jsonify({'prediction': str(prediction)})

    # except:

    #     return jsonify({'trace': traceback.format_exc()})


# ROUTE FOR RUNNING APP THROUGH BROWSWER REQUEST
@stats_routes.route("/predict_form", methods=["POST"])
def predict_html():
    print("PREDICT ROUTE...")
    # > {'screen_name_a': 'elonmusk', 'screen_name_b': 's2t2', 'tweet_text': 'Example tweet text here'}
    # print("FORM DATA:", dict(request.form))
    # # breakpoint()
    # category = request.form["category"]
    # pitch = request.form["pitch"]
    # a_ = int(request.form["a"])
    # b_ = int(request.form["b"])

    # # breakpoint()

    # # FOR TESTING PURPOSES ONLY - THE MODEL ONLY USES X AND Y FROM THE FORM
    # clf = load_model()
    # print("CLASSIFIER:", clf)
    # inputs = [[a_, b_]]
    # print(type(inputs), inputs)
    # result = clf.predict(inputs)
    # print("RESULT:", result)
    # print("-----------------")
    # print("*********** MAKING A PREDICTION...")

    # # breakpoint()

    # return jsonify({
    #     "message": "BOOK CREATED OK",
    #     "all features": dict(request.form),
    #     "feature used by model a": a_,
    #     "feature used by model b": b_,
    #     "predicted outcome: ": int(result[0])

    # })

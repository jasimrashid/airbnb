from flask import Blueprint, request, jsonify, render_template
import os
from sklearn.linear_model import LogisticRegression
import pandas as pd
import pickle

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


def load_model():
    print("LOADING THE MODEL...")
    # filename = '/Users/jasimrashid/Projects/DS-Unit-4-Build-Week-4-Airbnb/linear_model_pipeline_v2.pkl'
    filename = os.path.join(os.path.dirname(__file__),
                            "../..", "models", "decision_tree_model_fewer_features.pkl")
    # breakpoint()
    with open(filename, 'rb') as model_file:
        loaded_model = pickle.load(model_file)
    # breakpoint()
    return loaded_model


@ stats_routes.route("/predict", methods=["POST"])
def predict():
    print("PREDICTTTTTTTTTTTTTT ROUTE...")
    print("FORM DATA:", dict(request.form))
    # > {'screen_name_a': 'elonmusk', 'screen_name_b': 's2t2', 'tweet_text': 'Example tweet text here'}

    # TODO form elements: linear model k best
# input form variables

# input form variables

    # longitude = request.form['longitude']
    # latitude = request.form['latitude']

    # default values for Austin
    latitude = 30.2672
    longitude = 97.7431

    minimum_nights = int(request.form['minimum_nights'])
    maximum_nights = int(request.form['maximum_nights'])
    property_type = request.form['property_type']
    room_type = request.form['room_type']
    bathrooms = int(request.form['bathrooms'])
    accommodates = request.form['accommodates']
    bedrooms = int(request.form['bedrooms'])
    beds = int(request.form['beds'])
    bed_type = request.form['bed_type']
    transit_len = int(request.form['transit_len'])
    instant_bookable = request.form['instant_bookable']
    cancellation_policy = request.form['cancellation_policy']

    print('OK')

    # X_row = pd.DataFrame([[minimum_nights,  bathrooms, transit_len, maximum_nights, accommodates, property_type, room_type, instant_bookable, bed_type, cancellation_policy, bedrooms, beds, ]], columns=[
    #     'minimum_nights', 'bathrooms', 'transit_len', 'maximum_nights', 'accommodates', 'room_type', 'instant_bookable', 'bed_type', 'cancellation_policy', 'bedrooms', 'beds'])
    X_row = pd.DataFrame([[minimum_nights, transit_len, room_type, accommodates, longitude, bedrooms, instant_bookable, beds, bathrooms, maximum_nights, cancellation_policy, bed_type, latitude, property_type]], columns=[
                         'minimum_nights', 'transit_len', 'room_type', 'accommodates', 'longitude', 'bedrooms', 'instant_bookable', 'beds', 'bathrooms', 'maximum_nights', 'cancellation_policy', 'bed_type', 'latitude', 'property_type'])

    model = load_model()

    # breakpoint()
    y = model.predict(X_row)
    print('Prediction: ', y)

    # print("hello************", screen_name_a)
    # print("-----------------")
    # print("FETCHING TWEETS FROM THE DATABASE...")

    # TODO: load pretrained model

    print("-----------------")
    print("LOAD PRETRAINED MODEL...")

    # classifier = LogisticRegression()
    # # TODO: classifier.fit(___________, ___________)

    # breakpoint()
    print("-----------------")
    print("MAKING A PREDICTION...")

    # TODO

    return render_template("prediction_results.html",
                           y=y
                           )


if __name__ == "__main__":

    # linear_model = load_model()
    decision_tree_model = load_model()
    # TODO: use env variable
    X_train = pd.read_csv(
        '/Users/jasimrashid/Projects/DS-Unit-4-Build-Week-4-Airbnb/temp/x_train_100rows.csv', index_col=False)
    del X_train['Unnamed: 0']  # delete index
    print(decision_tree_model.predict(X_train))

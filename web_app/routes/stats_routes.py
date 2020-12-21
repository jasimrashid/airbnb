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
                            "../..", "models", "linear_model_pipeline_v2.pkl")
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
    require_guest_profile_picture = request.form['require_guest_profile_picture']
    minimum_nights = request.form['minimum_nights']
    bathrooms = int(request.form['bathrooms'])
    transit_len = int(request.form['transit_len'])
    maximum_nights = int(request.form['maximum_nights'])
    host_about_len = int(request.form['host_about_len'])
    accommodates = request.form['accommodates']
    property_type = request.form['property_type']
    room_type = request.form['room_type']
    interaction_len = int(request.form['interaction_len'])
    notes_len = int(request.form['notes_len'])
    instant_bookable = request.form['instant_bookable']
    bed_type = request.form['bed_type']
    access_len = int(request.form['access_len'])
    require_guest_phone_verification = request.form['require_guest_phone_verification']
    is_business_travel_ready = request.form['is_business_travel_ready']
    cancellation_policy = request.form['cancellation_policy']
    bedrooms = int(request.form['bedrooms'])
    metro_area = request.form['metro_area']
    beds = int(request.form['beds'])
    house_rules_len = int(request.form['house_rules_len'])

    # breakpoint()
    print('OK')

    X_row = pd.DataFrame([[require_guest_profile_picture, minimum_nights,  bathrooms, transit_len, maximum_nights, host_about_len, accommodates, property_type, room_type, interaction_len, notes_len, instant_bookable, bed_type, access_len, require_guest_phone_verification,  is_business_travel_ready, cancellation_policy, bedrooms, metro_area, beds, house_rules_len]], columns=[
        'require_guest_profile_picture', 'minimum_nights', 'bathrooms', 'transit_len', 'maximum_nights', 'host_about_len', 'accommodates', 'property_type', 'room_type', 'interaction_len', 'notes_len', 'instant_bookable', 'bed_type', 'access_len', 'require_guest_phone_verification', 'is_business_travel_ready', 'cancellation_policy', 'bedrooms', 'metro_area', 'beds', 'house_rules_len'])
    linear_model = load_model()

    # breakpoint()
    y = linear_model.predict(X_row)
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

    linear_model = load_model()
    # TODO: use env variable
    X_train = pd.read_csv(
        '/Users/jasimrashid/Projects/DS-Unit-4-Build-Week-4-Airbnb/x_train.csv')
    print(linear_model.predict(X_train))

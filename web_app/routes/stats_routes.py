from flask import Blueprint, request, jsonify, render_template
import os
from sklearn.linear_model import LogisticRegression
import pandas as pd
import pickle
import logging

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

metro_coord_mapping = {'Austin': (30.2672, -97.7431),
                       'Boston': (42.3601, -71.0589),
                       'Broward': (26.1901, -80.3659),
                       'Cambridge': (42.3736, -71.1097),
                       'Chicago': (41.8781, -87.6298),
                       'Twin Cities': (44.9375, -93.2010),
                       'Clark CO': (36.0796, -115.0940),
                       'Columbus': (39.9612, -82.9988),
                       'Denver': (39.7392, -104.9903),
                       'Hawaii': (19.8968, -155.5828),
                       'Jersey City': (40.7178, -74.0431),
                       'New York City': (40.7128, -74.0060),
                       'Los Angeles': (34.0522, -118.2437),
                       'Oakland': (37.8044, -122.2712),
                       'Nashville': (36.1627, -86.7816),
                       'New Orleans': (29.9511, -90.0715),
                       'Santa Clara': (37.3541, -121.9552),
                       'Portland': (45.5051, -122.6750),
                       'Rhode Island': (41.5801, -71.4774),
                       'Salem': (44.9429, -123.0351),
                       'San Diego': (32.7157, -117.1611),
                       'San Francisco': (37.7749, -122.4194),
                       'Seattle': (47.6062, -122.3321),
                       'Washington DC': (38.9072, -77.0369)}

extData = {'user': 'joem@example.com', 'boy': 'good'}


def load_model():
    print("LOADING THE MODEL...")
    # filename = '/Users/jasimrashid/Projects/DS-Unit-4-Build-Week-4-Airbnb/linear_model_pipeline_v2.pkl'
    # filename = os.path.join(os.path.dirname(__file__),
    #                         "../..", "models", "decision_tree_model_fewer_features.pkl")
    filename = os.path.join(os.path.dirname(__file__),
                            "../..", "models", "decision_tree_model-2.pkl")
    # breakpoint()
    with open(filename, 'rb') as model_file:
        loaded_model = pickle.load(model_file)
    # breakpoint()
    return loaded_model


@ stats_routes.route("/predict", methods=["POST"])
def predict():
    # print("PREDICTTTTTTTTTTTTTT ROUTE...")
    # print("FORM DATA:", dict(request.form))
    # > {'screen_name_a': 'elonmusk', 'screen_name_b': 's2t2', 'tweet_text': 'Example tweet text here'}

    # TODO form elements: linear model k best
    # input form variables

    # input form variables

    # longitude = request.form['longitude']
    # latitude = request.form['latitude']

    # default values for Austin
    # latitude = 30.2672
    # longitude = 97.7431

    metro_area = request.form['metro_area']
    latitude = metro_coord_mapping[metro_area][0]
    longitude = metro_coord_mapping[metro_area][1]

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

    print("model inputs: ", metro_area, latitude, longitude)

    X_train_row = {
        'maximum_nights': [maximum_nights],
        'room_type': [room_type],
        'longitude': [longitude],
        'cancellation_policy': [cancellation_policy],
        'bed_type': [bed_type],
        'transit_len': [transit_len],
        'bedrooms': [bedrooms],
        'minimum_nights': [minimum_nights],
        'property_type': [property_type],
        'latitude': [latitude],
        'beds': [beds],
        'bathrooms': [bathrooms],
        'instant_bookable': [instant_bookable],
        'accommodates': [accommodates]
    }

    # fmtStr = "%(minimum_nights)s, %(transit_len)s, %(room_type)s, %(accommodates)s, %(longitude)s, %(bedrooms)s, %(instant_bookable)s, %(beds)s, %(bathrooms)s, %(maximum_nights)s, %(cancellation_policy)s, %(bed_type)s, %(latitude)s, %(property_type)s"
    # logging.basicConfig(level=logging.DEBUG,filename="output.log",format=fmtStr)
    # logging.info("row: ", extra=X_train_row)

    X_row = pd.DataFrame([[maximum_nights, room_type, longitude, cancellation_policy, bed_type, transit_len, bedrooms, minimum_nights, property_type, latitude, beds, bathrooms, instant_bookable, accommodates]], columns=[
                         'maximum_nights', 'room_type', 'longitude', 'cancellation_policy', 'bed_type', 'transit_len', 'bedrooms', 'minimum_nights', 'property_type', 'latitude', 'beds', 'bathrooms', 'instant_bookable', 'accommodates'])

    print(X_train_row)

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

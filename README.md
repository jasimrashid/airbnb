
# Airbnb Pricing Predictions

![](/assets/arch_diagram_1.png)


INTRODUCTION

I've been an avid user of Airbnb since 2013. So I wanted to understand how Airbnb rental rates vary in the United States and what factors affect its prices. Although Airbnb does not expose its data through an API, there are commerical and non-commercial websites that scrape data and publish it for public use.

For my analysis I used [insiderairbnb.com's](http://insideairbnb.com/about.html) [1] datasets as a starting point. This website collects city-wide data from across the world, including more than a dozen U.S. metropolitain regions.

I also built a prediction tool that gives an estimate of an optimum price, based on the most important features. This prediction is based on a Random Forest regression model and trained on insiderairbnb's datasets. Finally, I hosted the prediction on AWS Heroku servers via a Flask web application and FastAPI.

The prediction can be accessed in this [heroku link](https://calm-plains-09823.herokuapp.com/)

![](/assets/prediction_form_2.png)

Here is an example of the end product
MODEL DEVELOPMENT


1. Model Development
    * Pre-processing & exploratory data analysis
    * Training the model

2. Model Deployment
    * Option A: Via Fast API
    * Option B: Via Heroku

3. Conclusion
    * Limitations
- seasonality; not based on time-series estimates
- supply and demand


[FastAPI for Flask Users](https://amitness.com/2020/06/fastapi-vs-flask/).

You'll build and deploy a Data Science API. You'll work cross-functionally with your Web teammates to connect your API to a full-stack web app!

Flask App Heroku link: [https://ds-bw-test.herokuapp.com/](https://ds-bw-test.herokuapp.com/)

## Model Development

### Pre-processing

Jupyter Notebook: [airbnb_eda_cycle_1.ipynb](notebooks/airbnb_eda_cycle_1.ipynb)

1. Clean errors in populated values
2. Explore data (examine distribution of data using boxplots and histograms)
3. Custom labeling: Classify all cities into 17 "metro area" categories

Exploratory data analysis - Charts:
![](/assets/eda_1.png)

Training the model

1. Split the data into training and test sets
```
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=.2, random_state=42)
```

2. Wrangle data and select features
``` 
target = ['price']

features = ['host_response_time','host_response_rate','host_acceptance_rate',
'street','neighbourhood','neighbourhood_cleansed','neighbourhood_group_cleansed','city','state','zipcode','market','smart_location','latitude','longitude','property_type','room_type','accommodates','bathrooms','bedrooms','beds','bed_type','amenities','square_feet','minimum_nights','maximum_nights','instant_bookable','is_business_travel_ready','cancellation_policy','require_guest_profile_picture','require_guest_phone_verification','notes_len','transit_len','access_len','interaction_len','house_rules_len','host_about_len','metro_area','bedrooms_str','beds_str']

# Wrangle and pre-process

# Removing sparse features from features (sparse features are <90% populated)
sparse_features = ['square_feet','neighbourhood_group_cleansed','host_response_rate','host_response_time','neighbourhood','host_acceptance_rate']

unusable_features = ['amenities']

duplicative_location_features = ['street','neighbourhood','neighbourhood_cleansed','neighbourhood_group_cleansed','city','state','zipcode','market','smart_location','metro_area']

numeric_columns = df.dtypes[df.dtypes==int].index.tolist()
nonnumeric_columns = df.dtypes[df.dtypes==object].index.tolist()

df[nonnumeric_columns] = df[nonnumeric_columns].astype(str)

selected_features = list(set(features) - set(sparse_features))
selected_features = list(set(selected_features) - set(unusable_features))
selected_features = list(set(selected_features) - set(duplicative_location_features))

df = df[target + selected_features]

df.dropna(inplace=True)
```
3. "Fit" the training set to models & choose model and parameters that has the "best" most optimal error metric
```
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
mae = mean_absolute_error(y_test, y_pred)
```

table showing MAE for various models

| Model          | Mean Absolute Error | xxxx     |
|:---            |                  | 123      |

| Model      | Mean Absolute Error | Size of Model     |
| :---        |    :----:   |          ---: |
| Baseline (Mean)      | 210       |    |
| Linear   | 179        | 47KB      |
| Ridge (α = .5)   | 169        | 179      |
| Ridge (α = .1)   | 167        | 179      |
| Decision Tree   | 134        | 20MB      |
| Random Forest   | 105        | >20MB      |

The best model has a low MAE but is also less likely to overfit/underfit outside the training set (mean-variance tradeoff) [1]. For the prediction tool, we'll choose a linear model because of its optimal size.

4. save chosen model as a pickle file

```
# Save pipeline 
with open('linear_model_pipeline_v2.pkl','wb') as model_file:
    pickle.dump(pipeline, model_file)
```


## Model Deployment

Predict optimal price for listings across the U.S. given a number of relevant features. 

### Technologies used

* Scikit learn
* Pandas
* Seaborn
* ....
* Regression models
* * 


### Installing the app:

Download the repo and navigate there from the command line:

```sh
git clone git@github.com:s2t2/twitoff-15.git
git clone https://github.com/jasimrashid/airbnb.git
cd airbnb
```

### Setup

Setup and activate a virtual environment:

```sh
pipenv install
pipenv shell
```
### Usage

Run the web app:

```sh
FLASK_APP=web_app flask run
```

### To Deploy to Heroku

Log in to Heroku from the CLI (first time only):
```sh
heroku login
```

Create a new application server (FROM WITHIN THE REPOSITORY'S ROOT DIRECTORY):
```sh
git remote -v
heroku create 
# optionally provide a name... "heroku create my-app-name"
git remote -v
```

Deploy to production:
```sh
git push heroku master
# or... git push heroku my_branch:master
```

### Notes & Sources


- Build week [team](https://buildweek.netlify.app/index.html)



    * Limitations
- seasonality; not based on time-series estimates
- supply and demand
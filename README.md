
# Airbnb Pricing Predictions

![](/assets/arch_diagram_1.png)


INTRODUCTION

I've been an avid user of Airbnb since 2013. So I wanted to understand how Airbnb rental rates vary in the United States and what factors affect its prices. Although Airbnb does not expose its data through an API, there are commerical and non-commercial websites that scrape data and publish it for public use.

For my analysis I used [insiderairbnb.com's](http://insideairbnb.com/about.html) [1] datasets as a starting point. This website collects city-wide data from across the world, including more than a dozen U.S. metropolitain regions.

I also built a prediction tool that gives an estimate of an optimum price, based on the most important features. This prediction is based on a Random Forest regression model and trained on insiderairbnb's datasets. Finally, I hosted the prediction on AWS Heroku servers via a Flask web application and FastAPI.

The prediction can be accessed in this [heroku link](https://calm-plains-09823.herokuapp.com/)

![](/assets/prediction_form_1.png)

Here is an example of the end product
MODEL DEVELOPMENT

1. Pre-processing

2. Training the model


3. Limitations
- seasonality; not based on time-series estimates
- supply and demand


[FastAPI for Flask Users](https://amitness.com/2020/06/fastapi-vs-flask/).

You'll build and deploy a Data Science API. You'll work cross-functionally with your Web teammates to connect your API to a full-stack web app!

Flask App Heroku link: [https://ds-bw-test.herokuapp.com/](https://ds-bw-test.herokuapp.com/)




## Tech stack
- [FastAPI](https://fastapi.tiangolo.com/): Web framework. Like Flask, but faster, with automatic interactive docs.
- [Flake8](https://flake8.pycqa.org/en/latest/): Linter, enforces PEP8 style guide.
- [Heroku](https://devcenter.heroku.com/): Platform as a service, hosts your API.
- [Pipenv](https://pipenv.pypa.io/en/latest/): Reproducible virtual environment, manages dependencies.
- [Plotly](https://plotly.com/python/): Visualization library, for Python & JavaScript.
- [Pytest](https://docs.pytest.org/en/stable/): Testing framework, runs your unit tests.

## Getting started

[Create a new repository from this template.](https://github.com/Lambda-School-Labs/ds-bw/generate)

Clone the repo
```
git clone https://github.com/YOUR-GITHUB-USERNAME/YOUR-REPO-NAME.git

cd YOUR-REPO-NAME
```

Install dependencies
```
pipenv install --dev

git add Pipfile.lock

git commit -m "Add Pipfile.lock"
```

Activate the virtual environment
```
pipenv shell
```

Launch the app
```
uvicorn app.main:app --reload
```

![image](https://user-images.githubusercontent.com/7278219/87965040-c18ba300-ca80-11ea-894f-d51a69d52f8a.png)

You'll see your API documentation:

- Your app's title, "DS API"
- Your description, "Lorem ipsum"
- An endpoint for POST requests, `/predict`
- An endpoint for GET requests, `/vis/{statecode}`

Click the `/predict` endpoint's green button.

![image](https://user-images.githubusercontent.com/7278219/87965845-0532dc80-ca82-11ea-9690-b4c195a648d6.png)

You'll see the endpoint's documentation, including:

- Your function's docstring, """Make random baseline predictions for classification problem."""
- Request body example, as [JSON](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects/JSON) (like a Python dictionary)
- A button, "Try it out"

Click the "Try it out" button.

![image](https://user-images.githubusercontent.com/7278219/87966677-39f36380-ca83-11ea-97f4-313bc11d3f19.png)

The request body becomes editable. 

Click the "Execute" button. Then scroll down.

![image](https://user-images.githubusercontent.com/7278219/87966896-948cbf80-ca83-11ea-9740-d0801148b1f3.png)

You'll see the server response, including:

- [Code 200](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/200), which means the request was successful.
- The response body, as [JSON](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects/JSON), with random baseline predictions for a classification problem.

***Your job is to replace these random predictions with real predictions from your model. Use this starter code and documentation to deploy your model as an API!***

## File structure

```
.
└── app
    ├── __init__.py
    ├── main.py
    ├── api
    │   ├── __init__.py
    │   ├── predict.py
    │   └── viz.py    
    └── tests
        ├── __init__.py
        ├── test_main.py
        ├── test_predict.py
        └── test_viz.py
```

`app/main.py` is where you edit your app's title and description, which are displayed at the top of the your automatically generated documentation. This file also configures "Cross-Origin Resource Sharing", which you shouldn't need to edit. 

- [FastAPI docs - First Steps](https://fastapi.tiangolo.com/tutorial/first-steps/)
- [FastAPI docs - Metadata](https://fastapi.tiangolo.com/tutorial/metadata/)
- [FastAPI docs - CORS](https://fastapi.tiangolo.com/tutorial/cors/)

`app/api/predict.py` defines the **Machine Learning** endpoint. `/predict` accepts POST requests and responds with random predictions. In a notebook, train your model and pickle it. Then in this source code file, unpickle your model and edit the `predict` function to return real predictions.

- [Scikit-learn docs - Model persistence](https://scikit-learn.org/stable/modules/model_persistence.html)
- [Keras docs - Serialization and saving](https://keras.io/guides/serialization_and_saving/)

When your API receives a POST request, FastAPI automatically parses and validates the request body JSON, using the `Item` class attributes and functions. Edit this class so it's consistent with the column names and types from your training dataframe. 

- [FastAPI docs - Request Body](https://fastapi.tiangolo.com/tutorial/body/)
- [FastAPI docs - Field additional arguments](https://fastapi.tiangolo.com/tutorial/schema-extra-example/#field-additional-arguments)
- [calmcode.io video - FastAPI - Json](https://calmcode.io/fastapi/json.html)
- [calmcode.io video - FastAPI - Type Validation](https://calmcode.io/fastapi/type-validation.html)
- [pydantic docs - Validators](https://pydantic-docs.helpmanual.io/usage/validators/)

`app/api/viz.py` defines the **Visualization** endpoint. Currently `/viz/{statecode}` accepts GET requests where `{statecode}` is a 2 character US state postal code, and responds with a Plotly figure of the state's unemployment rate, as a JSON string. Create your own Plotly visualizations in notebooks. Then add your code to this source code file. Your web developer teammates can use [react-plotly.js](https://github.com/Lambda-School-Labs/labs-spa-starter/tree/main/src/components/pages/ExampleDataViz) to show the visualizations.

![react-plotly.js animation](https://media.giphy.com/media/j3QG8qVBQcpKvCfO3T/giphy.gif)

- [Lambda School docs - Data visualization with React & Plotly](https://github.com/Lambda-School-Labs/labs-spa-starter/tree/main/src/components/pages/ExampleDataViz). This is the code for the above example. Your web teammates can reuse this as-is.
- [Plotly docs](https://plotly.com/python/)


`app/tests/test_*.py` is where you edit your pytest unit tests. 

- [FastAPI docs - Testing](https://fastapi.tiangolo.com/tutorial/testing/)
- [calmcode.io videos - FastAPI - Testing](https://calmcode.io/fastapi/testing-one.html)
- [calmcode.io videos - pytest](https://calmcode.io/pytest/introduction.html)

## More instructions

Activate the virtual environment
```
pipenv shell
```

Install additional packages
```
pipenv install PYPI-PACKAGE-NAME
```

Launch a Jupyter notebook
```
jupyter notebook
```

Run tests
```
pytest
```

Run linter
```
flake8
```

[calmcode.io videos - flake8](https://calmcode.io/flake8/introduction.html)

## Deploying to Heroku

Prepare Heroku
```
heroku login

heroku create YOUR-APP-NAME-GOES-HERE

heroku git:remote -a YOUR-APP-NAME-GOES-HERE
```

Deploy to Heroku
```
git add --all

git commit -m "Deploy to Heroku"

git push heroku main:master

heroku open
```

Deactivate the virtual environment
```
exit
```


# airbnb


Predict optimal price for listings across the U.S. given a number of relevant features. 

# Technologies used

* Scikit learn
* Pandas
* Seaborn
* ....
* Regression models
* * 


## Installing the app:

Download the repo and navigate there from the command line:

```sh
git clone git@github.com:s2t2/twitoff-15.git
git clone https://github.com/jasimrashid/airbnb.git
cd airbnb
```

## Setup

Setup and activate a virtual environment:

```sh
pipenv install
pipenv shell
```
## Usage

Run the web app:

```sh
FLASK_APP=web_app flask run
```

## To Deploy to Heroku

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

Notes & Sources


- Build week [team](https://buildweek.netlify.app/index.html)

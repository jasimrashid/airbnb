# airbnb pricing predictions

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





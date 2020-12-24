# airbnb

trying again

## Installation

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

Setup the database:

```sh
# Windows users can omit the "FLASK_APP=web_app" part...

FLASK_APP=web_app flask db init #> generates app/migrations dir

# run both when changing the schema:
FLASK_APP=web_app flask db migrate #> creates the db (with "alembic_version" table)
FLASK_APP=web_app flask db upgrade #> creates the specified tables
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





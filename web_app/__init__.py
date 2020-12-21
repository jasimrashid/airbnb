# web_app/__init__.py
from flask import Flask
import os
from dotenv import load_dotenv

from web_app.models import db, migrate

from web_app.routes.home_routes import home_routes
from web_app.routes.book_routes import book_routes
from web_app.routes.stats_routes import stats_routes

# load_dotenv

# No database
DATABASE_URI = os.getenv("DATABASE_URL")
SECRET_KEY = os.getenv("SECRET_KEY", default="super secret")

JASIM = 'BAD'

# using absolute filepath on Mac (recommended)
# DATABASE_URI = "sqlite:////Users/Username/Desktop/your-repo-name/airbnb_test.db"
# DATABASE_URI = "sqlite:///C:\\Users\\Username\\Desktop\\your-repo-name\\web_app_99.db" # using absolute filepath on Windows (recommended) h/t: https://stackoverflow.com/a/19262231/670433


def create_app():
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URI
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(home_routes)
    app.register_blueprint(book_routes)
    app.register_blueprint(stats_routes)

    # app.run(debug=True)

    return app


if __name__ == "__main__":
    my_app = create_app()
    my_app.run(debug=True)

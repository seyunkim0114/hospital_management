import os
import logging
import atexit

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import pymysql
from flask_cors import CORS

# from apscheduler.schedulers.background import BackgroundScheduler
# from apscheduler.triggers.cron import CronTrigger

from .routes import main, getNursesResponsibleForPrescriptionNow

# from apscheduler.schedulers.background import BackgroundScheduler
# from apscheduler.triggers.cron import CronTrigger



def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:iampw@localhost:3306/hospital_management'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    CORS(app)

    from .extensions import db, scheduler
    db.init_app(app)
    scheduler.init_app(app)
    scheduler.start()

    app.register_blueprint(main)

    

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    return app




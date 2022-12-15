import os
import logging
import atexit

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import pymysql
from flask_cors import CORS

# from apscheduler.schedulers.background import BackgroundScheduler
# from apscheduler.triggers.cron import CronTrigger
from flask_apscheduler import APScheduler

from .routes import main, getNursesResponsibleForPrescriptionNow
from .extensions import db

# from apscheduler.schedulers.background import BackgroundScheduler
# from apscheduler.triggers.cron import CronTrigger



def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:iampw@localhost:3306/hospital_management'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    CORS(app)
    db.init_app(app)
    # db.app = app

    app.register_blueprint(main)
    # with app.app_context():
    #     scheduler = APScheduler()
    #     scheduler.init_app(app)

    # # def scheduled():
    # #     with app.app_context():
    # #         getNursesResponsibleForPrescriptionNow()

    #     scheduler.add_job(id = "upcoming_prscp", func=getNursesResponsibleForPrescriptionNow, trigger="interval", seconds=5)
    #     scheduler.start()

    # app.logger.info(get_newclinicians())

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




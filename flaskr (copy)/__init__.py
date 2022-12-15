import os
import logging
import atexit

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import pymysql
from flask_cors import CORS

from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger


from .routes import main, getNursesResponsibleForPrescriptionNow
from .extensions import db

# from apscheduler.schedulers.background import BackgroundScheduler
# from apscheduler.triggers.cron import CronTrigger

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    # app.config.from_mapping(
    #     SECRET_KEY='dev',
    #     DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    # )
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:iampw@localhost:3306/hospital'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    CORS(app)
    db.init_app(app)

    app.register_blueprint(main)
    
    scheduler = BackgroundScheduler()
    # scheduler.start()
    scheduler.add_job(func=getNursesResponsibleForPrescriptionNow())
    # app.logger.info(get_newclinicians())
    atexit.register(lambda: scheduler.shutdown())  

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



# db = SQLAlchemy(app)

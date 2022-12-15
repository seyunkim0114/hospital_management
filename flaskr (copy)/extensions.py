from flask_sqlalchemy import SQLAlchemy
# from flask_apscheduler import APScheduler as _BaseAPScheduler

db = SQLAlchemy()

# class APScheduler(_BaseAPScheduler):
#     def run_job(self, id, jobstore=None):
#         with self.app.app_context():
#             super().run_job(id=id, jobstore=jobstore)
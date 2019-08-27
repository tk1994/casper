from celery import Celery
broker_url = 'amqp://prince:prince@localhost:5672//'
#pid,25182

# app = Celery('tasks', broker='amqp://prince:prince@localhost:5672/princehost')

# @app.task
# def add(x, y):
#     return x + y

# from __future__ import absolute_import, unicode_literals
# from celery import Celery


cel = Celery('src',
             broker='amqp://prince:prince@localhost:5672//',
             backend='db+sqlite3:///prince.status',
             include=['apis.file_download'])

# Optional configuration, see the application user guide.
cel.conf.update(
    result_expires=3600,
)

# if __name__ == '__main__':
#     app.start()

#-*-coding:utf-8-*-

from celery import Celery
import time

app = Celery('tasks',broker='redis://localhost',backend='redis://localhost')

@app.task
def job():
    if time.asctime()[17:19] == '10':
        return time.asctime()
    else:
        print 'not time'


            

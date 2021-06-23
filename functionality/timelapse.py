from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime


def capture_image(**kwargs):
    now = datetime.now()
    print(f'Taking an image at: {now}')


def timelapse(args):
    sched = BlockingScheduler()

    # Taking pictures
    sched.add_job(capture_image, trigger='cron', hour='9-16', second='*/30', id='timelapse', kwargs={'kwargs': args}, timezone='CET')
    sched.start()
    # Generating daily timelapses
    # sched.add_job(job_function, 'cron', month='6-8,11-12', day='3rd fri', hour='0-3')
    pass

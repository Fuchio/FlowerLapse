from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime
from pathlib import Path
import os
import cv2

img_count = 0

def capture_image(**kwargs):
    global img_count
    img_count += 1

    # Chech if path exists
    args = kwargs['kwargs']
    now = datetime.now()
    day = now.strftime("%d_%m")
    # TODO: Fix timelapse ID
    folder = args.path + '/' + args.timelapse_id + '/' + day + '/images'
    if not os.path.exists(folder):
        os.makedirs(folder)
    # Try to take image

    cam = cv2.VideoCapture(args.cam_id, cv2.CAP_DSHOW)
    if not cam:
        print(f'Failed VideoCapture: Invalid parameter {args.cam_id}')
    else:
        s, img = cam.read()
        if s:
            cv2.imwrite(folder + '/test_image_' + '%06d' % img_count + '.' + args.extension, img)
        else:
            print('Something went wrong taking the image, is the camera connected?')
        cam.release()

    # Try to save image
    print(f'Taking an image at: {now}')


def generate_timelapse(**kwargs):
    # Loop through folders containing images
    args = kwargs['kwargs']

    for path in Path('src').rglob('*.c'):
        print(path.name)
    pass
    # Use FFMPEG to save the timelapse


def timelapse(args):
    sched = BlockingScheduler(standalone=True)

    # Take one from the end_hour, if it has to stop at 17:00 the scheduler needs to be set at 16:00
    work_hours = str(args.start_hour) + '-' + str(args.end_hour - 1)
    timezone = args.timezone

    # Using an AND trigger with one CRON and one INTERVAL trigger is bugged in APScheduler 3. Tweak this software after APScheduler 4.0 release.
    if args.min_between != 0:
        minutes = '*/' + str(args.min_between)
        sched.add_job(capture_image, trigger='cron', hour=work_hours, minute=minutes, id='timelapse', kwargs={'kwargs': args}, timezone=timezone)
    else:
        seconds = '*/' + str(args.sec_between)
        sched.add_job(capture_image, trigger='cron', hour=work_hours, second=seconds, id='timelapse', kwargs={'kwargs': args}, timezone=timezone)



    try:
        sched.start()
    except (KeyboardInterrupt):
        print('Got SIGTERM! Terminating...')
        sched.shutdown(wait=False)

from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime
from pathlib import Path
import os
import cv2

img_count = 0

def create_path(args):
    '''
    Summary:
    Create directories to save all images and timelapses in.
    Returns the base directory.

    Inputs:
    ArgumentParser args : args.path and args.timelapse_id are used.

    Outputs:
    base_dir : Directory that serves as a base to save all images and timelapses.

    '''
    now = datetime.now()
    print(f'Taking an image at: {now}', flush=True)
    day = now.strftime("%d_%m")
    # TODO: Fix timelapse ID
    base_dir = args.path + '/' + args.timelapse_id + '/' + day
    img_dir = base_dir + '/images/'

    if not os.path.exists(img_dir):
        os.makedirs(img_dir)
    return base_dir


def capture_image(**kwargs):
    '''
    Summary:
    Job to capture new images and save them to disk with appropriate numbering.

    Inputs:
    ArgumentParser args : args.cam_id, args.extension are used

    Outputs:
    None. Images are saved to disk.
    '''
    global img_count
    img_count += 1

    # Chech if path exists
    args = kwargs['kwargs']
    base_path = create_path(args) + '/images'

    cam = cv2.VideoCapture(args.cam_id, cv2.CAP_DSHOW)
    if not cam:
        print(f'Failed VideoCapture: Invalid parameter {args.cam_id}')
    else:
        s, img = cam.read()
        if s:
            cv2.imwrite(base_path + '/image_' + '%06d' % img_count + '.' + args.extension, img)
        else:
            print('Something went wrong taking the image, is the camera connected?')
        cam.release()


def daily_timelapse(**kwargs):
    '''
    Summary:
    Function that is used by apscheduler to create a timelapse every day from all pics made that day.

    Inputs:
    ArgumentParser args : args.extension and args.fps are used.

    Outputs:
    None. Timelapse is saved to disk
    '''
    # Loop through folders containing images
    args = kwargs['kwargs']
    base_path = create_path(args)
    image_paths = Path(base_path).rglob('*' + args.extension)
    image_paths_sorted = sorted(image_paths, key=os.path.getmtime)

    fourcc = cv2.VideoWriter_fourcc('m','p','4','v')
    out = cv2.VideoWriter(base_path + '/daily_timelapse.mp4', fourcc, args.fps, (640,  480))

    for image_path in image_paths_sorted:
        frame = cv2.imread(str(image_path))
        out.write(frame)

    out.release()


def timelapse(args):
    '''
    Summary:
    Main function to handle the different scheduler jobs. Starts one job to create images and one to create timelapses.

    Inputs:
    ArgumentParser args : args.start_hour,
                          args.end_hour,
                          args.timezone,
                          args.min_between,
                          args.sec_between

    Outputs:
    None
    '''
    sched = BlockingScheduler(standalone=True)

    # Take one from the end_hour, if it has to stop at 17:00 the scheduler needs to be set at 16:00
    work_hours = str(args.start_hour) + '-' + str(args.end_hour - 1)
    timezone = args.timezone

    # Using an AND trigger with one CRON and one INTERVAL trigger is bugged in APScheduler 3. Tweak this software after APScheduler 4.0 release.
    if args.min_between != 0:
        minutes = '*/' + str(args.min_between)
        sched.add_job(capture_image, trigger='cron', hour=work_hours, minute=minutes, id='frame_gen', kwargs={'kwargs': args}, timezone=timezone)
    else:
        seconds = '*/' + str(args.sec_between)
        sched.add_job(capture_image, trigger='cron', hour=work_hours, second=seconds, id='frame_gen', kwargs={'kwargs': args}, timezone=timezone)

    sched.add_job(daily_timelapse, trigger='cron', hour='12', minute='15', id='daily_timelapse', kwargs={'kwargs': args}, timezone=timezone)

    try:
        sched.start()
    except (KeyboardInterrupt):
        print('Got SIGTERM! Terminating...')
        sched.shutdown(wait=False)
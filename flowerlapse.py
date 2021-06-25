from pathlib import Path
from datetime import datetime
import argparse
import cv2
import uuid

from functionality.test_camera import test_image, test_stream
from functionality.timelapse import timelapse

PATH = Path().resolve()
now = datetime.now()
day = now.strftime("%d_%m")

uuid = str(uuid.uuid1())
TIMELAPSE_ID = uuid[0:uuid.find('-')]

def main():
    parser = argparse.ArgumentParser()

    parser.add_argument('--cam_id',
                        type=int,
                        default=0,
                        help='ID of the camera that will be used. Default = 0, integrated webcam is usually 0 and if only one camera is connected the ID is always 0.')

    parser.add_argument('--timelapse_id',
                        type=str,
                        default=TIMELAPSE_ID,
                        help='ID that will be used to create a base directory to store images. Defaults to a generated ID.')

    parser.add_argument('--test_image',
                        default=False,
                        action='store_true',
                        help='Test the camera by taking a single image, image will be shown and saved to disk.')

    parser.add_argument('--test_stream',
                        default=False,
                        action='store_true',
                        help='Test the camera by displaying a videostream. Handy when placing the camera.')

    parser.add_argument('--sec_between',
                        type=int,
                        default=30,
                        help='Seconds between each image. Default at 30, mutually exclusive with min_between.')

    parser.add_argument('--min_between',
                        type=int,
                        default=0,
                        help='Minutes between each image. Defaults to 0 which means OFF, mutually exclusive with sec_between.')

    parser.add_argument('--start_hour',
                        type=int,
                        default=8,
                        help='Start taking pictures for the timelapse after 08:00 by default. Int between 0 and 23.')

    parser.add_argument('--end_hour',
                        type=int,
                        default=24,
                        help='Stop taking pictures for the timelapse after 24:00 by default. Int between 1 and 24.')

    parser.add_argument('--fps',
                        type=int,
                        default=30,
                        help='Frames per second for the timelapse. 24 or 30 is recommended. Default is 30.')

    parser.add_argument('--path',
                        type=str,
                        default=str(PATH),
                        help='Base path where all directories will be created. Default is current directory.')

    parser.add_argument('--timezone',
                        type=str,
                        default='CET',
                        help='Settable timezone for hour range, default is CET.')

    parser.add_argument('--extension',
                        type=str,
                        default='jpg',
                        help='Image extension, can be .jpg, .png or any OpenCV supported format. default is .jpg.')


    # Daily lapse ?
    # Weekly lapse ?
    # Monthly lapse ?
    # Total lapse ?


    args = parser.parse_args()

    if args.test_image:
        print('RUNNING: TEST_IMAGE')
        test_image(args)

    elif args.test_stream:
        print('RUNNING: TEST_STREAM')
        print('PRESS Q TO EXIT THE STREAM')
        test_stream(args)

    else:
        print('RUNNING: TIMELAPSE')
        timelapse(args)


if __name__ == '__main__':
    main()

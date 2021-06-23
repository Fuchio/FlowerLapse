from apscheduler.schedulers.blocking import BlockingScheduler
from pathlib import Path
import argparse
import cv2

from functionality.test_camera import test_image, test_stream
from functionality.timelapse import timelapse


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument('--cam_id',
                        type=int,
                        default=0,
                        help='ID of the camera that will be used. Default = 0, integrated webcam is usually 0 and if only one camera is connected the ID is always 0.')

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
                        help='Seconds between each image.')

    parser.add_argument('--start_hour',
                        type=int,
                        default=8,
                        help='Start taking pictures for the timelapse after 08:00 by default. Int between 0 and 23.')

    parser.add_argument('--end_hour',
                        type=int,
                        default=22,
                        help='Stop taking pictures for the timelapse after 22:00 by default. Int between 1 and 24.')


    # Save path
    # Timezone
    # Daily lapse (true/false)
    # Weekly lapse (true/false)
    # Monthly lapse ?
    # Total lapse ?


    # parser.add_argument('-t',
    #                     '--test_image',
    #                     type=str,
    #                     help='Base path where images and timelapses will be saved')

    args = parser.parse_args()

    if args.test_image:
        print('RUNNING: TEST_IMAGE')
        test_image(args)

    elif args.test_stream:
        print('RUNNING: TEST_STREAM')
        print('PRESS Q TO EXIT THE STREAM')
        test_stream(args)

    else:
        timelapse(args)


if __name__ == '__main__':
    main()

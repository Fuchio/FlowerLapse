from pathlib import Path
import cv2
import argparse

PATH = Path().resolve()

def list_clips(args):
    path = args.path / args.timelapse_id

    tl_list = Path(path).rglob('daily_timelapse.mp4')
    tl_list_sorted = sorted(img_list, key=os.path.getmtime)
    for tl_path in tl_list_sorted:
        print(tl_path)

def main():
    parser = argparse.ArgumentParser()

    parser.add_argument('--timelapse_id',
                        type=str,
                        help='ID that was used to create a base directory to store images. Check your base dir for the generated ID.',
                        required=True)

    parser.add_argument('--path',
                        type=str,
                        default=str(PATH),
                        help='Base path where all directories were created. Default is current directory. Supply the path if it was used in ')

    parser.add_argument('--start_date',
                        type=str,
                        help='Date to start the concatenated timelapse.')

    parser.add_argument('--end_date',
                        type=str,
                        help='Date to end the concatenated timelapse.')

    args = parser.parse_args()

if __name__ == '__main__':
    main()

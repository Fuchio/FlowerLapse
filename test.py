from pathlib import Path
import os
import cv2

PATH = Path().resolve()
PATH = PATH / 'eafbf869' / '27_06'

img_list = Path(PATH).rglob('*.jpg')
img_list = sorted(img_list, key=os.path.getmtime)
for img_path in img_list:
    print(img_path)

fourcc = cv2.VideoWriter_fourcc('m','p','4','v')
out = cv2.VideoWriter('timelapse.mp4', fourcc, 30, (640,  480))

for image_path in img_list:
    frame = cv2.imread(str(image_path))
    out.write(frame)
#
# out.release()

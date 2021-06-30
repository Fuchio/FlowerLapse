import cv2
from datetime import datetime

def add_overlay(image):
    '''
    Summary:
    Adds the current date and time to the top left corner and flowerlapse to
    the bottom right corner.

    Inputs:
    image : OpenCV Image

    Outputs:
    image : OpenCV Image with overlay
    '''
    now = datetime.now()
    timestamp = now.strftime("%d/%m/%y - %H:%M")

    dim = image.shape

    top_left = (5, 30)
    bottom_left = (5, dim[0] - 10)

    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(image, timestamp, top_left, font, 1, (0, 0, 0), 2, cv2.LINE_AA)
    cv2.putText(image, 'FlowerLapse', bottom_left, font, 1, (0, 200, 0), 2, cv2.LINE_AA)

    return image

import cv2

def test_image(args):
    cam = cv2.VideoCapture(args.cam_id)
    if not cam:
        print(f'Failed VideoCapture: Invalid parameter {args.cam_id}')
    else:
        s, img = cam.read()
        if s:
            cv2.imshow("cam-test",img)
            cv2.waitKey(0)
            cv2.imwrite("test_image.jpg",img)
            cam.release()
            cv2.destroyAllWindows()
        else:
            print('Something went wrong taking the image, is the camera connected?')


def test_stream(args):
    cam = cv2.VideoCapture(args.cam_id)
    if not cam:
        print(f'Failed VideoCapture: Invalid parameter {args.cam_id}')
    else:
        while(True):
            s, img = cam.read()

            cv2.imshow("cam-test",img)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        cam.release()
        cv2.destroyAllWindows()

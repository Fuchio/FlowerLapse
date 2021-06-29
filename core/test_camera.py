import cv2

def test_image(args):
    '''
    Summary:
    Function to take a test image and save to drive. Saves image at
    <file root> / test_image.jpg

    Inputs:
    ArgumentParser args : args.cam_id and args.extension are used

    Outputs:
    None. Saves at <file root> / test_image.jpg
    '''
    cam = cv2.VideoCapture(args.cam_id)
    if not cam:
        print(f'Failed VideoCapture: Invalid parameter {args.cam_id}')
    else:
        s, img = cam.read()
        if s:
            cv2.imshow("cam-test",img)
            cv2.waitKey(0)
            cv2.imwrite("test_image." + args.extension, img)
            cam.release()
            cv2.destroyAllWindows()
        else:
            print('Something went wrong taking the image, is the camera connected?')


def test_stream(args):
    '''
    Summary:
    Function to show a test stream, useful when placing the camera.

    Inputs:
    ArgumentParser args : args.cam_id is used

    Outputs:
    None. Opens new window to show cam outputs
    '''
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

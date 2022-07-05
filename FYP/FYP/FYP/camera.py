import cv2


WHITE = [255, 255, 255]
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalcatface.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')


def draw_box(Image, x, y, w, h):
    cv2.line(Image, (x, y), (x + int(w / 5), y), WHITE, 2)
    cv2.line(Image, (x + int((w / 5) * 4), y), (x + w, y), WHITE, 2)
    cv2.line(Image, (x, y), (x, y + int(h / 5)), WHITE, 2)
    cv2.line(Image, (x + w, y), (x + w, y + int(h / 5)), WHITE, 2)
    cv2.line(Image, (x, (y + int(h / 5 * 4))), (x, y + h), WHITE, 2)
    cv2.line(Image, (x, (y + h)), (x + int(w / 5), y + h), WHITE, 2)
    cv2.line(Image, (x + int((w / 5) * 4), y + h), (x + w, y + h), WHITE, 2)
    cv2.line(Image, (x + w, (y + int(h / 5 * 4))), (x + w, y + h), WHITE, 2)


class VideoCamera(object):
    def __init__(self):
        self.video = cv2.VideoCapture(0)

    def __del__(self):
        self.video.release()


    def get_frame(self):
        success, image = self.video.read()
        # We are using Motion JPEG, but OpenCV defaults to capture raw images,
        # so we must encode it into JPEG in order to correctly display the
        # video stream.

       
        #oswaldo's comment
        if success == True:
            ret, jpeg = cv2.imencode('.jpg', image)
            if ret == True:
                return jpeg.tobytes()

    def capture_1_pic(self):
        return_value, image = self.video.read()
        cv2.imwrite('FYP/FYP/FYP/static/images/loginpic.jpg', image)
           
        self.video.release()

    def capture_10_pics(self):
        for i in range(10):
            return_value, image = self.video.read()
            cv2.imwrite('FYP/FYP/FYP/static/images/opencv'+str(i)+'.jpg', image)
           
        self.video.release()

    def stop_camera(self):
        self.video.release()
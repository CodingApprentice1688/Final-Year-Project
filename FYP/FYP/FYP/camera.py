import cv2
from mtcnn import MTCNN
import mediapipe as mp


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
        
        minDetectionCon=0.5
        self.minDetectionCon = minDetectionCon
 
        self.mpFaceDetection = mp.solutions.face_detection
        self.mpDraw = mp.solutions.drawing_utils
        self.faceDetection = self.mpFaceDetection.FaceDetection(self.minDetectionCon)
        self.video = cv2.VideoCapture(0)
        self.video.set(cv2.CAP_PROP_FRAME_WIDTH, 850)
        self.video.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

 
    def findFaces(self, img, draw=True):
 
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.faceDetection.process(imgRGB)
        # print(self.results)
        bboxs = []
        if self.results.detections:
            for id, detection in enumerate(self.results.detections):
                bboxC = detection.location_data.relative_bounding_box
                ih, iw, ic = img.shape
                bbox = int(bboxC.xmin * iw), int(bboxC.ymin * ih), \
                       int(bboxC.width * iw), int(bboxC.height * ih)
                if draw:
                    img = self.fancyDraw(img,bbox)
        return img
 
    def fancyDraw(self, img, bbox):
        x, y, w, h = bbox
        x1, y1 = x + w, y + h
 
        cv2.rectangle(img, bbox, (0, 255, 0), 3)
        return img

    def __del__(self):
        self.video.release()


    def get_frame(self):
        success, image = self.video.read()
        
        #detector = MTCNN()
        detector = VideoCamera()
        pTime = 0
        
       
        #oswaldo's comment
        if success == True:

            image = detector.findFaces(image)
            #results = detector.detect_faces(image)
            #if results:
            #    x1, y1, width, height = results[0]['box']
            #    # bug fix
            #    x1, y1 = abs(x1), abs(y1)
            #    # extract the face
            #    cv2.rectangle(image, (x1, y1, width, height), (255, 0, 255), 3)
            ret, jpeg = cv2.imencode('.jpg', image)
            
            if ret == True:
                return jpeg.tobytes()

    def capture_1_pic(self):
        return_value, image = self.video.read()
        cv2.imwrite('FYP/FYP/FYP/static/images/loginpic.jpg', image)
           
        self.video.release()

    def capture_10_pics(self):
        for i in range(25):
            return_value, image = self.video.read()
            cv2.imwrite('opencv'+str(i)+'.jpg', image)
           
        self.video.release()

    def stop_camera(self):
        self.video.release()
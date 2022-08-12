import cv2
from mtcnn import MTCNN
import mediapipe as mp
import time
import os
from threading import Thread


#WHITE = [255, 255, 255]
#face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalcatface.xml')
#eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')


#def draw_box(Image, x, y, w, h):
#    cv2.line(Image, (x, y), (x + int(w / 5), y), WHITE, 2)
#    cv2.line(Image, (x + int((w / 5) * 4), y), (x + w, y), WHITE, 2)
#    cv2.line(Image, (x, y), (x, y + int(h / 5)), WHITE, 2)
#    cv2.line(Image, (x + w, y), (x + w, y + int(h / 5)), WHITE, 2)
#    cv2.line(Image, (x, (y + int(h / 5 * 4))), (x, y + h), WHITE, 2)
#    cv2.line(Image, (x, (y + h)), (x + int(w / 5), y + h), WHITE, 2)
#    cv2.line(Image, (x + int((w / 5) * 4), y + h), (x + w, y + h), WHITE, 2)
#    cv2.line(Image, (x + w, (y + int(h / 5 * 4))), (x + w, y + h), WHITE, 2)


class VideoCamera(object):
    def __init__(self):
        
        minDetectionCon=0.5
        self.minDetectionCon = minDetectionCon
 
        self.mpFaceDetection = mp.solutions.face_detection
        self.mpDraw = mp.solutions.drawing_utils
        self.faceDetection = self.mpFaceDetection.FaceDetection(self.minDetectionCon)
        self.video = cv2.VideoCapture(0)
        self.video.set(cv2.CAP_PROP_FRAME_WIDTH, 700)
        self.video.set(cv2.CAP_PROP_FRAME_HEIGHT, 400)
        self.video.set(cv2.CAP_PROP_FPS, 30)
        self.video.set(cv2.CAP_PROP_BUFFERSIZE, 3)
        
        
        # Start frame retrieval thread
        #self.thread = Thread(target=self.get_frame, args=())
        #self.thread.daemon = True
        #self.thread.start()

 
       

    def __del__(self):
        self.video.release()


    def get_frame(self):
        success, image = self.video.read()
        
        #detector = MTCNN()
        #pTime = 0
        
       
        #oswaldo's comment
        if success == True:
            try:
                imgRGB = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
                self.results = self.faceDetection.process(imgRGB)
                draw = True
                # print(self.results)
                bboxs = []
                if self.results.detections:
                    for id, detection in enumerate(self.results.detections):
                        bboxC = detection.location_data.relative_bounding_box
                        ih, iw, ic = image.shape
                        bbox = int(bboxC.xmin * iw), int(bboxC.ymin * ih), \
                               int(bboxC.width * iw), int(bboxC.height * ih)
                        if draw:
                             x, y, w, h = bbox
                             x1, y1 = x + w, y + h
 
                             cv2.rectangle(image, bbox, (0, 255, 0), 3)
            except:
                pass
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
        self.video.release()
        cv2.destroyAllWindows()

    def capture_1_pic(self):
        return_value, image = self.video.read()
        cv2.imwrite('FYP/static/images/loginpic.jpg', image)
           
        self.video.release()
        cv2.destroyAllWindows()

    def capture_one_pic(self, username):
        path = "pati"
        try:
            os.makedirs("FYP/static/" + path)
        except:
            pass

        return_value, image = self.video.read()
        cv2.imwrite('FYP/static/pati/' + str(username) + '.jpg', image)
        self.video.release()
        cv2.destroyAllWindows()
           

    def capture_10_pics(self, username):
        path = "temp"
        try:
            os.makedirs("FYP/static/" + path)
        except:
            pass

        last_recorded_time = time.time()
        i = 0
        while True:
            curr_time = time.time()
            return_value, image = self.video.read()
            if curr_time - last_recorded_time >= 0.3 and i < 25: 
                cv2.imwrite('FYP/static/temp/'+ str(i) + str(username) + '.jpg', image)
                last_recorded_time = curr_time
                i = i + 1
            elif i >= 25:
                break
        self.video.release()
        cv2.destroyAllWindows()

        #last_recorded_time = time.time()
        #for i in range(1000):
        #    curr_time = time.time()
        #    if curr_time - last_recorded_time >= 2.0 and i < 25: 
        #        return_value, image = self.video.read()
        #        cv2.imwrite('opencv'+str(i)+'.jpg', image)
        #        last_recorded_time = curr_time
        #    elif i >= 25:
        #        break
        #self.video.release()

    def stop_camera(self):
        self.video.release()
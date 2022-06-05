#Face tracker using OpenCV and Arduino
#by Shubham Santosh

import cv2
import serial,time
import argparse

parser = argparse.ArgumentParser(description='Code for FaceTrackCam.')
parser.add_argument('--camera', '-cam', help='Camera divide number.', type=int, default=0)
parser.add_argument('--comPort', '-com', help='Arduino COM port number.', type=str, default='com3')
args = parser.parse_args()

# face_cascade= cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cap=cv2.VideoCapture(args.camera)
#fourcc= cv2.VideoWriter_fourcc(*'XVID')
ArduinoSerial=serial.Serial(args.comPort,9600,timeout=0.1)
#out= cv2.VideoWriter('face detection4.avi',fourcc,20.0,(640,480))
time.sleep(1)

# with open('face.names', 'r') as f:
#     classes = f.read().splitlines()

net = cv2.dnn.readNetFromDarknet('yolov4-tiny-obj.cfg', 'yolov4-tiny-obj_last.weights')
model = cv2.dnn_DetectionModel(net)
model.setInputParams(scale=1 / 255, size=(416, 416), swapRB=True)

while cap.isOpened():
    ret, frame= cap.read()
    frame=cv2.flip(frame,1)  #mirror the image
    # frame = cv2.resize(frame, (416, 416))
    #print(frame.shape)
    # gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    # faces= face_cascade.detectMultiScale(gray,1.1,6)  #detect the face
    classIds, scores, faces = model.detect(frame, confThreshold=0.6, nmsThreshold=0.4)
    if len(faces)!=0:
        max=-1
        target=0
        for idx, (x, y, w, h) in enumerate(faces):
            if w*h > max:
                max = w*h
                target = idx
            #plot the center of the face
            cv2.circle(frame,(x+w//2,y+h//2),2,(0,255,0),2)
            #plot the roi
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),3)
            


        x, y, w, h = faces[target]
        # sending coordinates to Arduino
        string='X{0:d}Y{1:d}'.format((x+w//2),(y+h//2))
        print(string)
        ArduinoSerial.write(string.encode('utf-8'))
        
        
        #cv2.imwrite('output_img.jpg',frame)
        
        # for testing purpose
        # read= str(ArduinoSerial.readline(ArduinoSerial.inWaiting()))
        # time.sleep(0.05)
        # print('data from arduino:'+read)
        
        # press q to Quit
    cv2.rectangle(frame,(640//2-70,480//2-70),
                        (640//2+70,480//2+70),
                        (255,255,255),3)
    #out.write(frame)
    cv2.imshow('img',frame)
    if cv2.waitKey(10)&0xFF== ord('q'):
        break
cap.release()
cv2.destroyAllWindows()

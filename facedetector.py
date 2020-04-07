import cv2
import sys

faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

eyeCascade = cv2.CascadeClassifier('haarcascade_eye.xml')
# Using the webcam
video_capture = cv2.VideoCapture(0)
img_counter = 0

while True:
    # Capture frame by frame
    ret, frame = video_capture.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)# Convert BGR to GRAY
    k = cv2.waitKey(1)
    faces = faceCascade.detectMultiScale(
            gray,
            scaleFactor = 1.5,
            minNeighbors = 5,
            minSize = (30, 30),
            flags = cv2.CASCADE_SCALE_IMAGE
            )
    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x,y),(x+w, y+h), (0,255,255),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
        eyes = eyeCascade.detectMultiScale(roi_gray,1.3,5)
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
        

    # Display the resulting frame
    cv2.imshow("FaceDetection", frame)

    if k%256 == 27: # ESC Pressed
        break
    elif k%256 == 32: # Space Pressed
        img_name = "facedetect_webcam_{}.png".format(img_counter)
        cv2.imwrite(img_name, frame)
        print("{} written".format(img_name))
        img_counter +=1

# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()
        
    

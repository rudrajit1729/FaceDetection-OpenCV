# FaceDetection-OpenCV

Face Detection for the  the identification of human faces in digital images or video. It can be regarded as a specific case of object-class detection, where the task is to find the locations and sizes of all objects in an image that belongs to a given class. 

 The technology is able to detect frontal or near-frontal faces in a photo, regardless of orientation, lighting conditions or skin color.
 Also includes detection of eye for those given faces.
 Run *faceDetector.py* having the XMLs in the same directory to test the program. 
 
 For the purpose we will be using haarcascade classifiers.
 
# What is Haar Cascades?
Object Detection using Haar feature-based cascade classifiers is an effective object detection method proposed by Paul Viola and Michael Jones in their paper, “Rapid Object Detection using a Boosted Cascade of Simple Features” in 2001.

# Haar-cascade Detection in OpenCV
OpenCV comes with a trainer as well as a detector. If you want to train your own classifier for any object like a car, planes, etc. you can use OpenCV to create one. Its full details are given here: Cascade Classifier Training.
Here we will deal with detection. OpenCV already contains many pre-trained classifiers for face, eyes, smile, etc. Those XML files are stored in opencv/data/haarcascades/ Folder. 

github link : https://github.com/opencv/opencv/tree/master/data/haarcascades

Additional read : For face recognition using eigenfaces and SVMs
                  Link : http://scikit-learn.sourceforge.net/0.6/auto_examples/applications/plot_face_recognition.html


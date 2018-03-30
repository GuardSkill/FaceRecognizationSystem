import face_recognition
import cv2
import pickle

one_img = face_recognition.load_image_file("FacePicture/silicon_valley.jpg")
one_encoding = face_recognition.face_encodings(one_img)[0]

class Info(object):
    name = 'anoymous'
    encoding = one_encoding
    admin = 0

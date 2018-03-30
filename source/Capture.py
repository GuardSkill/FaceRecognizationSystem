# -*- coding: utf-8 -*-
#
# 检测人脸
import face_recognition
import cv2
import pickle
from pick_class import Info
#face_locations = face_recognition.face_locations(img)
#Returns::A list of tuples of found face locations in css (top, right, bottom, left) order
#Given an image, return the 128-dimension face encoding for each face in the image.
info=Info()
info.name='LiSiyuan'
info.admin=1
fn     = 'data.pkl'
datalist=[info]
if __name__=='__main__':
    with open(fn, 'wb') as f:  # open file with write-mode
        pickle.dump(datalist, f, fix_imports=False)  # serialize and save object
        # del info
        # info = pickle.load(f)   # read file and build object
    video_capture = cv2.VideoCapture(0)

# coding=utf-8
import cv2
import numpy as np
import pickle
import matplotlib.pyplot as plt

# 获取默认摄像头
cap = cv2.VideoCapture(0)
index = 0
while True:
    # 获取视频
    ret, frame = cap.read()
    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Display the resulting frame
    cv2.imshow('frame', gray)

    if cv2.waitKey(1) & 0xFF == ord('p'):
        cv2.imwrite("F:\pick.jpg", frame)
        index = index + 1
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
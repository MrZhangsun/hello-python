# coding=utf-8
import cv2
import numpy as np

cap = cv2.VideoCapture(0)

# Define the codec and create VideoWriter object
fourcc = cv2.cv.FOURCC(*'XVID')

out = cv2.VideoWriter('F:\output.mp4', fourcc, 20.0, (800, 600))

while cap.isOpened():
    ret, frame = cap.read()
    if ret is True:
        # 第二个参数控制图形的方向1，向上，0向下
        frame = cv2.flip(frame, 1)
        out.write(frame)
        cv2.imshow("test", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
out.release()
cv2.destroyAllWindows()

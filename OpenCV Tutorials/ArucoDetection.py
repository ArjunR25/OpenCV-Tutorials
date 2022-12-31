import cv2
import cv2.aruco as aruco
import numpy as np

dictionary = aruco.Dictionary_get(aruco.DICT_6X6_250)
parameters = aruco.DetectorParameters_create()

# frame = cv2.imread('singlemarkersoriginal.jpg', cv2.IMREAD_COLOR)
# cv2.imshow('frame', frame)
# print('frame')

cap = cv2.VideoCapture(0) # cv2.VideoCapture(2)
while(True):
    ret, frame = cap.read()
    # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # out.write(frame)
    # cv2.imshow('frame', frame)
    corners, ids, rej = aruco.detectMarkers(frame, dictionary, parameters=parameters)

    # final = np.copy(frame)
    # cv2.imshow('final', final)
    aruco.drawDetectedMarkers(frame, corners, ids)
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()


# cv2.imshow('final', final)
# cv2.waitKey(0)
# cv2.destroyAllWindows()



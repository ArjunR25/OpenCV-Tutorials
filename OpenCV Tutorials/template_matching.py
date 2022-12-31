import cv2
import numpy as np

img = cv2.imread('target.jpg')
# template = cv2.imread('template.jpg')

# res = cv2.matchTemplate(img,template,cv2.TM_CCOEFF_NORMED)
# threshold = 0.14
# loc = np.where( res >= threshold)

# for pt in zip(*loc[::-1]):
#     cv2.circle(img, pt, 10, (0,255,0), -1)

# _, img = video.read()

roi = cv2.imread('template.jpg')
# roi = cv2.imread('/content/drive/MyDrive/CV Pics/Barrel.png', 1)
hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
hsv_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)


roi_hist = cv2.calcHist([hsv_roi], [0, 1], None, [180, 256], [0, 180, 0, 256])
normalized = cv2.normalize(roi_hist, np.zeros((180, 256)), 0, 255, cv2.NORM_MINMAX)  
res = cv2.calcBackProject([hsv_img], [0, 1], roi_hist, [0, 180, 0, 256], 1)
disc = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
res = cv2.filter2D(res, -1, disc)
ret, thresh = cv2.threshold(res, 75, 255, cv2.THRESH_BINARY)

kernel = np.ones((21, 21))
thresh = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)
final = cv2.merge((thresh,thresh,thresh))
result = cv2.bitwise_or(img, final)

cv2.imshow('Detected', result)
cv2.waitKey(0)
cv2.destroyAllWindows()
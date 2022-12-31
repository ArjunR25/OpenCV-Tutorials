import cv2
import matplotlib.pyplot as plt

img = cv2.imread('watch.jpg',cv2.IMREAD_GRAYSCALE)
# IMREAD_GRAYSCALE = 0
# IMREAD_COLOR = 1
# IMREAD_UNCHANGED = -1

#NOTE: cv2 images are in BGR format while PLT treats them in RGB
# cv2.imshow('image',img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

print(img.shape) # (rows, columns) = (168, 300)

plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
plt.plot([50,100],[100,150],'c', linewidth=5) # x coords, y coords
plt.show()

cv2.imwrite('watchgray.png',img)
import cv2
import numpy as np

img = cv2.imread("low_contrast_image.jpeg",0)
contra = cv2.equalizeHist(img)
result = np.hstack((img,contra))
cv2.imwrite('result.jpg', result)
cv2.imshow('eqalized',result)
cv2.waitKey(0)   
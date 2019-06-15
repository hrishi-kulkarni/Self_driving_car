import cv2
import numpy as np

im_gray = cv2.imread('fffe248a-3f38-11e8-9edf-68140106f352_0.jpg', 0)
#img = cv2.blur(img, (5, 5))
#retval, img = cv2.threshold(img, 140, 255, cv2.THRESH_BINARY)
im_gray = cv2.resize(im_gray, (25, 25))
#image_as_array = np.ndarray.flatten(np.asarray(img))
(thresh, im_bw) = cv2.threshold(im_gray, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

cv2.imshow('img',im_bw)
cv2.waitKey(0)
cv2.destroyAllWindows()
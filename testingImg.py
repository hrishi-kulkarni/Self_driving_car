from skimage import io
import cv2
img = io.imread('http://192.168.225.35:8080')
cv2.imshow('title', img)
cv2.waitkey(0)
cv2.destroyAllWindows()
import cv2
import numpy as np

img = cv2.imread('img/black_500.jpg')
#윗반구
cv2.ellipse(img, (250, 250), (200, 200), 0, 181, 360, (0, 0, 201), -1, cv2.LINE_AA)
#아래반구
cv2.ellipse(img, (250, 250), (200, 200), 0, 0, 180, (255, 255, 255), -1, cv2.LINE_AA)
cv2.ellipse(img, (250, 250), (200, 50), 0, 0, 360, (0, 0, 201), -1, cv2.LINE_AA)
cv2.ellipse(img, (250, 250), (205, 50), 0, 0, 180, (0, 0, 0), 7, cv2.LINE_AA)
cv2.ellipse(img, (250, 297), (70, 70), 0, 0, 360, (255, 255, 255), -1, cv2.LINE_AA)
cv2.ellipse(img, (250, 297), (70, 70), 0, 0, 360, (0, 0, 0), 7, cv2.LINE_AA)
cv2.ellipse(img, (250, 297), (30, 30), 0, 0, 360, (0, 0, 0), 5, cv2.LINE_AA)

cv2.imshow('result',img)

cv2.waitKey(0)
cv2.destroyAllWindows()
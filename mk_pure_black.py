import cv2
import numpy as np
img = np.zeros((500,500,3), dtype=np.uint8)
cv2.imshow("result", img)
cv2.waitKey(0)
cv2.imwrite("img\\black_500.jpg", img)
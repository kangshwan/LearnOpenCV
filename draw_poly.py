import cv2
import numpy as np

img = cv2.imread('../blank_500.jpg')

#Numpy 배열로 좌표 생성
#번개모양 선 좌표
pts1 = np.array([[50, 50], [150, 150], [100, 140], [200, 240]], dtype=np.int32)
#삼각형 좌표
pts2 = np.array([[350, 50], [250, 200], [450, 200]], dtype=np.int32)
#삼각형 좌표
pts3 = np.array([[150, 300], [50, 450], [250, 450]], dtype=np.int32)
#오각형 좌표
pts4 = np.array([[350, 250], [450, 350], [400, 450], [300, 450], [250, 350]], dtype=np.int32)
cv2.polylines(img, [pts1], False, (255, 0, 0))
cv2.polylines(img, [pts2], False, (0, 0, 0), 10)
cv2.polylines(img, [pts3], True, (200, 150, 30), 10)
cv2.polylines(img, [pts4], True, (100, 150, 30), 1)
#rectangular을 그리는것 처럼 선 굵기에 -1을 넣어보았으나, 되지 않았다.

cv2.imshow('polyline', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
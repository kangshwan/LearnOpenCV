#-*- coding:utf-8 -*-

import cv2
import numpy
# 한글경로가 imread로 되지 않아서, 다른방법을 사용했다.
# imread는 결국 numpy 배열로 return 하는것이기 때문에
# bytearray타입으로 byte를 읽어온뒤 numpy로 convert해준다.
# 먼저 파일경로를 연 뒤, numpyarray로 만들고 cv2로 decode한다.
print(cv2.__version__)

def koreanPath( file_path ):
    
    stream = open(file_path.encode("utf-8"), "rb")
    bytes = bytearray(stream.read())
    numpyArray = numpy.asarray(bytes, dtype=numpy.uint8)

    #return cv2.imdecode(numpyArray, cv2.IMREAD_UNCHANGED)  """그대로 읽기"""
    return cv2.imdecode(numpyArray, cv2.IMREAD_GRAYSCALE)   #회색으로 읽어오기
    #return cv2.imdecode(numpyArray, cv2.IMREAD_COLOR)   #컬러스케일로 읽어오기


img_file = "C:\\Users\\rnltl\\Desktop\\VISUALCODE\\openCV\\picachu.jpg"

save_file = "C:\\Users\\rnltl\\Desktop\\VISUALCODE\\openCV\\picachu_gray.jpg"

img = cv2.imread(img_file, cv2.IMREAD_GRAYSCALE)
cv2.imshow(img_file, img)
cv2.imwrite(save_file, img)
cv2.waitKey()
cv2.destroyAllWindows()
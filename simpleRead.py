import cv2
import numpy

def koreanPath( file_path ):
    
    stream = open(file_path.encode("utf-8"), "rb")
    bytes = bytearray(stream.read())
    numpyArray = numpy.asarray(bytes, dtype=numpy.uint8)

    return cv2.imdecode(numpyArray, cv2.IMREAD_UNCHANGED)


print(cv2.__version__)
img_file = "C:\\Users\\rnltl\\OneDrive\\바탕 화면\\VISUALCODE\\openCV\\픽가츄.jpg"
img = koreanPath(img_file)
print(img_file)
if img is not None:
    cv2.imshow('IMG', img)
    cv2.waitKey()
    cv2.destroyAllWindows()
else:
    print('No image file.')
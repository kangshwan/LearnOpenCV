import cv2

video_file = "C:\\Users\\rnltl\\Desktop\\VISUALCODE\\openCV\\Overwatch.mp4"

cap = cv2.VideoCapture(video_file)

if cap.isOpened():
    while True:
        ret, img = cap.read()
        if ret:
            cv2.imshow(video_file, img)
            cv2.waitKey(10)
        else:
            break
else:
    print("can't open video.")
cap.release()
cv2.destroyAllWindows()
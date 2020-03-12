import cv2

video_file = "C:\\Users\\rnltl\\Desktop\\VISUALCODE\\openCV\\maple.mp4"

cap = cv2.VideoCapture(video_file)

if cap.isOpened():
    while True:
        ret, img = cap.read()
        if ret:
            cv2.imshow(video_file, img)
            if cv2.waitKey(25) != -1:
                cv2.imwrite('photo.jpg', img)
                break
        else:
            break
else:
    print("can't open video.")
cap.release()
cv2.destroyAllWindows()
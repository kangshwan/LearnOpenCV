import cv2

video_file = "C:\\Users\\rnltl\\Desktop\\VISUALCODE\\test1.avi"

cap = cv2.VideoCapture(0)      #캡쳐객체 생성
if cap.isOpened():                      #캡쳐객체 초기화 확인
    fps = cap.get(cv2.CAP_PROP_FPS)     #프레임 수 구하기
    delay = int(1000/fps)           
    print("FPS: %f, Delay: %dms" %(fps, delay))

    while True:
        ret, img = cap.read()             #다음 프레임 읽기
        if ret:
            cv2.imshow(video_file, img)
            cv2.waitKey(delay) != -1
        else:
            break
else:
    print("Can't open video.")
cap.release()                           #캡쳐 자원 반납
cv2.destroyAllWindows()

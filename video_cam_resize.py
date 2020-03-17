import cv2

# cap = cv2.VideoCapture(0)       #카메라 0번 장치 연결
# 카메라가 아닌 동영상 파일에 프레임 크기를 재지정하는 것은 적용이 안된다고 한다...

cap = cv2.VideoCapture(0)

width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)           #프레임 폭 값
height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)         #프레임 높이 값
print("Original width: %d, height: %d" %(width, height))

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 320)              # 프레임 폭을 320으로 설정
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)             # 프레임 폭을 240으로 설정
width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)           # 재 지정한 프레임 폭 값
height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)         # 재 지정한 프레임 높이 값
print("Resized width: %d, height: %d" %(width, height))

if cap.isOpened():
    while True:
        ret, img = cap.read()
        print(ret)
        if ret:
            cv2.imshow('CAMERA', img)
            if cv2.waitKey(1) != -1:
                break
        else:
            print('no frame!')
            break
else:
    print("can't open camera")
cap.release()
cv2.destroyAllWindows()

#
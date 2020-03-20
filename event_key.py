import cv2

img_file = "./img/picachu.jpg"
img = cv2.imread(img_file)
title = 'IMG'           #창이름
x, y = 100, 100         #최초 좌표

while True:
    cv2.imshow(title, img)
    cv2.moveWindow(title, x, y)
    key = cv2.waitKey(0) & 0xFF #키보드 입력을 무한 대기, 8bit 마스크 처리
    print(key, chr(key))        #키보드 입력값, 문자값 출력
    if key == ord('h'):         # 'h' 이면 좌로 이동
        x -= 10
    elif key == ord('j'):       # 'j' 이면 아래로 이동
        y += 10
    elif key == ord('k'):       # 'k' 이면 위로 이동
        y -= 10
    elif key == ord('l'):       # 'l' 이면 우로 이동
        x += 10
    elif key == ord('q') or key == 27:  # 'q' 이거나 'esc'이면 종료
        break
        cv2.destroyAllWindows()
    cv2.moveWindow(title, x, y) # 새로운 좌표로 창 이동
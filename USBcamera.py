# -*- coding:utf-8 -*-
#webカメラの映像から顔を探し白の枠線をつけて保存するプログラム

import cv2
import threading
# カメラをキャプチャ開始
cap = cv2.VideoCapture(0)
size = (400,300)

def red_track(frame):
    step = 1
    for y in range(0,len(frame[0]),step):
        for x in range(0,len(frame),step):
            # rv = int(r-((g*b)/2))
            # if rv < 0 : rv = 0
            frame[x][y] = [frame[x][y][0],frame[x][y][0],frame[x][y][0]]
    return frame

while True:
    global size
    ret, frame = cap.read()

    if True:
            frame = frame[:,::-1]

    if size is not None and len(size) == 2:
                frame = cv2.resize(frame, size)

    # frame = red_track(frame)

    #frameを表示
    cv2.imshow('camera capture', frame)

    #10msecキー入力待ち
    k = cv2.waitKey(10)
    #Escキーを押されたら終了
    if k == 27:
        break

#キャプチャを終了
cap.release()
cv2.destroyAllWindows()
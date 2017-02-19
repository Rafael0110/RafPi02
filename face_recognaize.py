# -*- coding:utf-8 -*-
import cv2

# cv2.cv.CV_FOURCC
def cv_fourcc(c1, c2, c3, c4):
    return (ord(c1) & 255) + ((ord(c2) & 255) << 8) + \
        ((ord(c3) & 255) << 16) + ((ord(c4) & 255) << 24)


if __name__ == '__main__':

	ESC_KEY = 27     # Escキー
	INTERVAL= 33     # 待ち時間
	FRAME_RATE = 60  # fps

	CANNY_WINDOW_NAME = "canny"
	DEVICE_ID = 0

	# カメラ映像取得
	cap = cv2.VideoCapture(DEVICE_ID)

	# 保存ビデオファイルの準備
	end_flag, c_frame = cap.read()

	# ウィンドウの準備
	cv2.namedWindow(CANNY_WINDOW_NAME)

	# ウィンドウの準備
	cv2.namedWindow(CANNY_WINDOW_NAME)


	# 顔認識用特徴量のファイル指定
	cascade_path = "haarcascades/haarcascade_frontalface_alt.xml"

	# カスケード分類器の特徴量を取得する
	cascade = cv2.CascadeClassifier(cascade_path)

	while end_flag == True :

		gray_frame = cv2.cvtColor(c_frame, cv2.COLOR_BGR2GRAY)
		facerecog = cascade.detectMultiScale(gray_frame, scaleFactor=1.1, minNeighbors=1, minSize=(1, 1))

		#　認識した顔を囲む矩形の色を指定。ここでは白。
		color = (255, 255, 255) 

		cv2.rectangle(facerecog, tuple(rect[0:2]),tuple(rect[0:2]+rect[2:4]), color, thickness=2)

		cv2.imshow(CANNY_WINDOW_NAME, facerecog)

		# Escキーで終了
		key = cv2.waitKey(INTERVAL)
		if key == ESC_KEY: break

		# 次のフレーム読み込み
		end_flag, c_frame = cap.read()

		cv2.destroyAllWindows()
		cap.release()
		rec.release()
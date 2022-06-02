# 追蹤人臉 WebCam (YOLOv4_tiny + Arduino servo)

## reference: https://create.arduino.cc/projecthub/shubhamsantosh99/face-tracker-using-opencv-and-arduino-55412e

PC端使用python OpenCV匯入YOLOv4_tiny模型偵測人臉，再透過pyserial套件與arduino溝通。

本篇使用Arduino Uno來控制兩顆servo馬達，自動調整鏡頭的角度，讓人臉盡量維持在鏡頭中心

原作者使用Harr cascade of classifiers 來做人臉偵測 -> 速度慢，精確度不高

所以我改使用YOLOv4_tiny來偵測人臉，達到即時偵測的性能，且精確度明顯提升

# 訓練

YOLOv4_tiny: 利用darknet以資料集WIDER FACE (http://shuoyang1213.me/WIDERFACE/) 進行訓練。可參考: https://medium.com/ching-i/yolo-c49f70241aa7



# 待改進

yolo 使用GPU可以大大提升FPS

但openCV只能用CPU，如果要使用GPU必須安裝額外的擴充套件
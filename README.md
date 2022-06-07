# 追蹤人臉 WebCam (YOLOv4_tiny + Arduino servo)

## reference: https://create.arduino.cc/projecthub/shubhamsantosh99/face-tracker-using-opencv-and-arduino-55412e

* 利用python OpenCV匯入YOLOv4_tiny模型偵測人臉，再透過pyserial套件傳送座標給arduino。

* 本篇使用Arduino Uno控制兩顆servo馬達，自動調整鏡頭的角度，讓人臉盡量維持在鏡頭中心

* 原作者以Harr cascade of classifiers 來做人臉偵測 -> 速度慢，精確度不高。所以我改以YOLOv4_tiny偵測人臉，達到即時偵測的性能，且精確度明顯提升

* 原作者沒有對同時有多個臉的情況作處理，可能導致鏡頭來回晃動。所以我加了以下判斷: 如果同時偵測到多個臉，以最近的臉為目標(面積最大的bounding box)

![image](./demo/demo2.gif)

# 訓練

YOLOv4_tiny: 利用darknet以資料集WIDER FACE (http://shuoyang1213.me/WIDERFACE/) 進行訓練。可參考: https://medium.com/ching-i/yolo-c49f70241aa7



# 待改進

yolo 在GPU執行可以大大提升FPS

但openCV只能用CPU，如果要在GPU執行必須安裝額外的擴充套件
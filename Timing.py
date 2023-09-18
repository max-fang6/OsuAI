import keras
from ultralytics import YOLO
import numpy as np
import cv2
from PIL import ImageGrab
from pyautogui import click
from keras.models import Sequential
from keras.layers import LSTM

##Locator_model = YOLO('yolov8n.yaml')
##results = Locator_model.train(data=r'D:\project-2-at-2023-08-23-18-59-84ef5770\Data\config.yml',
##                              epochs=20, imgsz=1280, patience=5)

model = Sequential()

##Outside Circle = [x1, x2], Circle = [c1, c2], Time = t
##Input = ([x1, x2], [c1, c2], t)
model.add(LSTM(50, activation='relu', input_shape=(2,3)))



bounding_box = (0, 0, 1080, 1920)
Frame_no = 1
Hit_times = {}
Frame2 = 0
while True:
    Frame_no += 1
    print(Frame_no)
    if Frame_no in Hit_times.keys():
        ##let x_value = x from output of model etc.
        x_value, y_value = Hit_times.get(Frame_no)
        pyautogui.click(x=320 + x_value, y=180 + y_value)
        Hit_times.pop(Frame_no)

    ## Bounding box should take the form (left, top, right, bottom)
    sct_img = ImageGrab.grab(bounding_box)
    cv2.imshow('screen', np.array(sct_img))
    ##insert model to find boxes
    if Frame2 != 0:

    ##insert model to calculate Hit_time and add it to Hit_times using sct_img and Frame2
    Frame2 = sct_img

    if (cv2.waitKey(1) & 0xFF) == ord('q'):
        cv2.destroyAllWindows()
        break






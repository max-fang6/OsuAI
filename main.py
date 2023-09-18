import keras
from ultralytics import YOLO
import numpy as np
import cv2
from PIL import ImageGrab
from pyautogui import click
from keras.models import Sequential
from keras.layers import LSTM


model = YOLO('yolov8n.pt')
model = YOLO(r'D:\best.pt')

bounding_box = (640, 360, 1280, 720)  #These dimensions are set to the smallest native resolution of the game for my monitor
Frame_no = 1
Hit_times = {}
Frame2 = 0
while True:
    Frame_no += 1
    if Frame_no in Hit_times.keys():
        ##let x_value = x from output of model etc.
        x_value, y_value = Hit_times.get(Frame_no)
        pyautogui.click(x=320 + x_value, y=180 + y_value)
        Hit_times.pop(Frame_no)

    sct_img = pyautogui.screenshot(region = bounding_box)
    results = model.predict(sct_img, imgsz=1280, conf=0.7, stream=True)
    cv2.imshow('screen', np.array(sct_img))
    ##insert model to find boxes
    if Frame2 == 0:
        Frame2 = sct_img
        continue

    ##Function responsible for pairing boxes together will be used here
    ##LSTM prediction will be used here

    Frame2 = sct_img

    if (cv2.waitKey(1) & 0xFF) == ord('q'):
        cv2.destroyAllWindows()
        break





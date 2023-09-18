from ultralytics import YOLO
from PIL import Image
import pyautogui


'''
This file takes screenshots in an infinite while loop
and detects whether or not timing and hit circles are detected. The coordinates are then added with 
the class value to a dict with key Frame_no and value 
(array([class_no, ...], dtype=float32), array([[xyxy], ...], dtype=float32)).
The images are also saved as Frame_no.jpg.
write_txt takes the dict as input and saves the keys and values in the following form
Frame_no, (array([class_no, ...], dtype=float32), array([[xyxy], ...], dtype=float32))
to a .txt file 
'''

model = YOLO('yolov8n.pt')
model = YOLO(r'D:\best.pt')

bounding_box = (640, 360, 1280, 720)
Frame_no = 0
coordinates = {}

while True:
    Frame_no += 1
    print(Frame_no)
    sct_img = pyautogui.screenshot(region=bounding_box)

    results = model.predict(sct_img, imgsz=1280, conf=0.7, stream=True)
    for objects in results:
        print(objects.boxes)
        if len(objects.boxes) != 0:
            sct_img.save(fp=r'D:\LSTM\{title}.jpg'.format(title=Frame_no))
            coordinates.update({Frame_no: (objects.boxes.cls.numpy(), objects.boxes.xyxy.numpy())})

    if Frame_no == 300:
        break

write_txt(coordinates)

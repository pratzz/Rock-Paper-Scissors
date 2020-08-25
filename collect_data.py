import numpy as np
import cv2
import os
import sys
import time

label_map = {
    "0": "Rock",
    "1": "Paper",
    "2": "Scissors"
} 
print("Please select one of the labels:")
print("Rock(0)")
print("Paper(1)")
print("Scissors(2)")
label = label_map.get(input(f"Your input: "))
if not label:
    print("Label not specified")
print("\n"+label,"selected!")


PATH = os.getcwd()+'\\'
cap = cv2.VideoCapture(0)
SAVE_PATH = os.path.join(PATH, label)

if not os.path.exists(SAVE_PATH):
    os.mkdir(SAVE_PATH)
    
num_imgs = int(input(f"No. of images do you wish to capture:"))
print("Hit Space to Capture Image")

count = 0
while True:
    ret, frame = cap.read()
    cv2.imshow('Collecting Data : '+label,frame)
    if cv2.waitKey(1) & 0xFF == ord(' '):
        curr_time = time.strftime("%Y%m%d-%H%M%S")
        cv2.imwrite(SAVE_PATH+'\\'+label+'_{}.jpg'.format(curr_time),frame)
        print(SAVE_PATH+'\\'+label+'_{}.jpg Captured'.format(curr_time))
        count+=1
    if count >= num_imgs:
        break

cap.release()
cv2.destroyAllWindows()

import numpy as np
from PIL import ImageGrab
import cv2
import time
import pyautogui
from directkey import PressKey, W, A, S, D 

for i in list(range(4))[::-1]:
        print(i+1)
        time.sleep(1)

print('down')
PressKey(W) 
time.sleep(3)
print('up')
PressKey(W)

def process_img(image):
 
    original_image = image
    #BGR TO GRAY because the [0,255,255] is bgr and [0,8,8] is gray for simpler data manipulation
    processed_img = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)
    processed_img= cv2.Canny(processed_img, 200, 300)
    return processed_img

last_time = time.time()

while(True):
        # 800x600 windowed mode
    screen =  np.array(ImageGrab.grab(bbox=(0,40,800,640)))
    new_screen = process_img(screen)

    print('loop took {} seconds'.format(time.time()-last_time))
    last_time = time.time()
    cv2.imshow('window', new_screen)
   # cv2.imshow('window2',cv2.cvtColor(printscreen, cv2.COLOR_BGR2RGB))
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break

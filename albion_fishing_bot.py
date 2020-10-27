import numpy as np
import cv2
import cv
from mss.linux import MSS as mss
from PIL import Image
import time
import pyautogui as pg
import imutils
import mss
import numpy
import pyautogui

template = cv2.imread("float_2.png", cv2.IMREAD_GRAYSCALE)
w, h = template.shape[:: - 1]

color_yellow = (70, 120, 35)

mon = {'top': 50, 'left': 600, 'width': 110, 'height': 110}


def process_image(original_image):
    processed_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)

    processed_image = cv2.Canny(processed_image, threshold1=200, threshold2=300)
    return processed_image


def ss():
    op = 1
    with mss.mss() as sct:

        monitor = {"top": 40, "left": 30, "width": 800, "height": 640}

        while "Screen capturing":
            img = numpy.array(sct.grab(monitor))

            gray_frame = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            res = cv2.matchTemplate(gray_frame, template, cv2.TM_CCOEFF_NORMED)
            loc = np.where(res >= 0.7)
            op += 1

            print('op:', op)
            for pt in zip(*loc[::-1]):
                cv2.rectangle(img, pt, (pt[0] + w, pt[1] + h), (0, 255, 0), 3)
                for p in img:
                    pts = (pt[0], pt[1])
                    x = (pt[0])
                    y = (pt[1])
                    print('pos', x)
                    if x >= 680:
                        pyautogui.mouseDown(button='left')
                        time.sleep(0.5)
                        pyautogui.mouseUp(button='left')
                        break
                    elif 627 < x < 680:
                        pyautogui.mouseDown(button='left')
                        time.sleep(1)
                        pyautogui.mouseUp(button='left')
                        break
                    elif 596 < x <= 627:
                        pyautogui.mouseDown(button='left')
                        time.sleep(1.753)
                        pyautogui.mouseUp(button='left')
                        break
                    elif 100 < x <= 596:
                        pyautogui.mouseDown(button='left')
                        if op <= 3:
                            time.sleep(1.4)
                        else:
                            time.sleep(2.63)
                        pyautogui.mouseUp(button='left')
                        break
                    else:
                        continue
                else:
                    continue
                break

            key = cv2.waitKey(1)
            if cv2.waitKey(25) & 0xFF == ord("q"):
                cv2.destroyAllWindows()
            if op > 30:
                return


def screen_record():
    sct = mss.mss()
    last_time = time.time()

    while True:
        img = sct.grab(mon)
        print('loop took {} seconds'.format(time.time() - last_time))
        last_time = time.time()

        img = np.array(img)
        processed_image = process_image(img)

        mean = np.mean(processed_image)
        print('mean =', mean)

        if mean <= float(0.14):
            print('Fish')
            pyautogui.click(button='left')
            break
        else:
            time.sleep(0.01)
            continue
            return

    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        return


while True:
    time.sleep(1)
    pyautogui.moveTo(660, 260, duration=1)
    pyautogui.mouseDown(button='left')
    pyautogui.moveTo(670, 270, duration=1)
    pyautogui.mouseUp(button='left')
    time.sleep(1)

    screen_record()
    time.sleep(0.01)

    ss()

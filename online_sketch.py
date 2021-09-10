#program by Akshayjyoti Bordoloi
#testing date: September 10, 2021

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time
import random
import pyautogui

points = int(input("Enter number of points: "))

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://sketch.io/sketchpad/')
driver.set_window_position(0,0)
driver.set_window_size(1600,1000)
time.sleep(2)

pyautogui.moveTo(1850,10)
pyautogui.click()
time.sleep(1)

pyautogui.moveTo(450, 300)
pyautogui.click()
time.sleep(1)

x_ini = random.randint(400,1600)
y_ini = random.randint(200,800)
pyautogui.moveTo(x_ini, y_ini)
pyautogui.mouseDown()
for i in range(points-1):
    x = random.randint(400,1600)
    y = random.randint(200,800)
    pyautogui.moveTo(x,y, duration = 1)
    time.sleep(1)
pyautogui.moveTo(x_ini, y_ini, duration = 1)
pyautogui.mouseUp()

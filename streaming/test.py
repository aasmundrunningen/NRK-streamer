from selenium import webdriver
import keyboard
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome()
driver.get("https://tv.nrk.no/direkte/nrk1")
actions = ActionChains(driver)
driver = webdriver.Chrome(ChromeDriverManager().install())

startPlay = driver.find_element(By.CLASS_NAME,"ludo-poster-button")
try:
    startPlay.click()
except:
    None
#playWindow = driver.find_element(By.CLASS_NAME,"ludo-layout")
#playWindow.send_keys("f")


while True:
    try:
        #test = driver.find_element(By.CLASS_NAME,"ludo-layout__row ludo-controlbar")
        print(True)
    except:
        print(False)


sleep(20)
actions.send_keys("f")
actions.perform()   
print("fullscreen")

#|startPlay = driver.find_element("ludo-poster__play-progress")

# while True:
#     #startPlay = driver.find_element(By.CLASS_NAME, "ludo-layout")
#     try:
#         startPlay = driver.find_element(By.CLASS_NAME,"ludo-poster__play-progress")
#         print(startPlay.is_displayed())
#         if startPlay.is_displayed():
#             startPlay.click()
#             print("started Video")
#         # if startPlay.is_visible():
#         #     print("paused")
#         # else:
#         #     print("playing")
#     except:
#         print("error")

# while True:
    # try:
    #     playbutton = driver.find_element_by_class_name("ludo-bar__button ludo-playicon ludo-playicon--play")
    #     print("paused")

    # except:
        # try:
        #     startPlay = driver.find_element_by_class("ludo-poster__play-progress")
        #     print("paused")
        # except:
        #     print("playing")
    # sleep(3)
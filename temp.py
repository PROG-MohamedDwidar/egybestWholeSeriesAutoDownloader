# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.action_chains import ActionChains

def hoomock(driver:webdriver.Chrome):#for hooman mocker "used to fool adblocker detector by actually watching the ad :'("
    while(True):
        elm=driver.find_element(By.XPATH,"//a[@class='bigbutton _reload']")
        elm.click()
        #preventing getting detected by adblocker detection by openning the ad
        driver.switch_to.window(driver.window_handles[2])
        ad=WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, "/html/head/title")))
        while(ad.text=='Redirect'):
            ad=WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, "/html/head/title")))
        driver.switch_to.window(driver.window_handles[1])

        try:
            elm=WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.XPATH, '//a[@href^="https"]')))
            break
        except Exception:
            pass
        elm=driver.find_element(By.XPATH,"//a[@class='bigbutton _reload']")


def downep(url):
    drivep=webdriver.Chrome('C:\webdrivers\chromedriver.exe')
    getweb(drivep,url)
    
    # downlink=drivep.find_element(By.CLASS_NAME,'nop btn g dl _open_window')
    downlink=WebDriverWait(drivep, 10).until(EC.presence_of_element_located((By.NAME, 'q')))
    downlink.click()
    print("stage:101")
    drivep.switch_to.window(drivep.window_handles[1])
    ad=WebDriverWait(drivep, 3).until(EC.presence_of_element_located((By.XPATH, "/html/head/title")))
    while(ad.text=='Redirect'):
        ad=WebDriverWait(drivep, 3).until(EC.presence_of_element_located((By.XPATH, "/html/head/title")))



    drivep.switch_to.window(drivep.window_handles[0])
    downlink=drivep.find_elements(By.XPATH,"//a[@class='nop btn g dl _open_window']")
    print(len(downlink))
    downlink[1].click()
    time.sleep(0.2)
    drivep.switch_to.window(drivep.window_handles[1])
    try:
        bigfinale=WebDriverWait(drivep, 1).until(EC.presence_of_element_located((By.XPATH, '//a[@href^="https"]')))
    except Exception:
        bigfinale=WebDriverWait(drivep, 3).until(EC.presence_of_element_located((By.XPATH, "//a[@class='bigbutton _reload']")))
        hoomock(drivep)
        bigfinale=WebDriverWait(drivep, 1).until(EC.presence_of_element_located((By.XPATH, '//a[@href^="https"]')))
    
    #*********************special moment*************************************
    bigfinale.click()


    
    

    




def getweb(driver:webdriver,url):
    try:
        driver.get(url)
    except Exception:
        getweb(driver, url)
    
start=int(input("enter episode number where u want to start downloading:"))
end=int(input("enter episode number where u want to stop downloading (the one you enter is included):"))
#-----------------------------------------------------------------#
# Open browser and facebook code
driver = webdriver.Chrome('C:\webdrivers\chromedriver.exe')  
getweb(driver, "https://poly.egybest.me/episode/suits-arabic-season-1-ep-13/")


driver.implicitly_wait(5)
#-----------------------------------------------------------------#
# get a list with all episodes
# search=driver.find_element(By.CLASS_NAME,'movies_small')
search=WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'movies_small')))
listEps=search.find_elements(By.CLASS_NAME,'movie')

current=len(listEps)
for i in listEps:
    if(current>=start and current<=end):
        link=i.get_attribute('href')
        try:
            downep(link)
        except Exception:
            pass
    current-=1







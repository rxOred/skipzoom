#!/usr/bin/python3

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#from fake_useragent import UserAgent
from time import sleep
import json
import undetected_chromedriver as uc
from datetime import datetime
import schedule
import pyautogui
import cv2
import numpy as np
import threading

'''
by,
        ▄▄▄  ▄▄▄ .·▄▄▄▄  ▄▄▄  ▪        ▄▄▄▄▄
        ▀▄ █·▀▄.▀·██▪ ██ ▀▄ █·██ ▪     •██  
        ▐▀▀▄ ▐▀▀▪▄▐█· ▐█▌▐▀▀▄ ▐█· ▄█▀▄  ▐█.▪
        ▐█•█▌▐█▄▄▌██. ██ ▐█•█▌▐█▌▐█▌.▐▌ ▐█▌·
        .▀  ▀ ▀▀▀ ▀▀▀▀▀• .▀  ▀▀▀▀ ▀█▄▀▪ ▀▀▀ 
'''
class recorder:
    
    def __init__(self):
        self.resolution = (1024,768)
        self.codec = cv2.VideoWriter_fourcc(*'XVID')
        
        self.file = "class.avi"
        self.frames_per_second = 30.0
        
        self.o = cv2.VideoWriter(self.file, self.codec, self.frames_per_second, self.resolution) 
        
    def run(self):
        try:
            cv2.namedWindow('Live', cv2.WINDOW_NORMAL)
            cv2.resizeWindow("Live", 120, 100)
            
            while True:
                self.img = pyautogui.screenshot()
                self.frame = np.array(self.img)
                self.frame = cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB)
                
                self.o.write(self.frame)
                #cv2.imshow('recorder', self.frame)
                
                if driver.title == "Error - Zoom":
                    break
                elif driver.title == 'Profile - Zoom':
                    break
                
        except :
            print("my camera is broken")
                #elif driver.title == 
    #def run_thread(self):
        #self.thred = threading.Thread(target=self.run)
        #self.thred.start()

def join(link, code):
    r = recorder()
    rec = threading.Thread(target=r.run)
    rec.start()
    
    print(driver.title)
    join_the_meeting = driver.find_element_by_id("btnJoinMeeting")
    join_the_meeting.click()
    
    join_confo = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.ID, 'join-confno')))

    #join_confo = driver.find_element_by_id("join-confno")
    join_confo.send_keys(link)
    join_confo.send_keys(Keys.ENTER)
    
    sleep(5)
    
    try:
        launch_meetin = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@class='_3Gj8x8oc']")))
        launch_meetin.click()
        
        use_Browser = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//h3[2]/a[1]")))
        use_Browser.click()
        
        join_button = driver.find_element_by_id("joinBtn")
        join_button.send_keys(Keys.ENTER)
        
        join_button2 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'wc_vanity_url_join')))
        join_button2.click()
        
        passw = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@id='inputpasscode']")))
        passw.send_keys(code)
        passw.send_keys(Keys.ENTER)
        
    except:
        print("something is wrong i can feel it")
    
    #name_fill = driver.find_element_by_id("inputname")
    #name_fill.send_keys("Jayod")
    #sleep(3)
    #name_fill.send_keys(Keys.ENTER)
    #joinbtn = driver.find_element_by_id("joinBtn").click()     
    
def enterCreds(usr, password, link, code):
    try:
        email = driver.find_element_by_id('email')
        email.clear()
        email.send_keys(usr)
        sleep(2)

        passwd = driver.find_element_by_id("password")
        #passwd.clear()
        passwd.send_keys(password)
        sleep(1)
        passwd.send_keys(Keys.ENTER)
        
    except Exception as e:
        print(e)  
        #enterCreds(usr, password, link, code)
        
    print(driver.title)
    sleep(10)
    if driver.title == "My Profile - Zoom":
        join(link, code)
        
def job():
    
    data = json.load(open('links.json'))
    link = data['classid']
    code = data['classpw']
    
    login = json.load(open("creds.json"))
    usr = login['user']
    password = login['pass']
    #options = Options()
    #userAg = UserAgent()
    #ua = userAg.random
    #options.add_argument('user-agent={}'.format(ua))
    
    driver.get("https://us05web.zoom.us/profile")

    if driver.title == 'Sign In - Zoom':
        enterCreds(usr, password, link, code)
        
    elif driver.title == 'My Profile - Zoom':
        join(link, code)
        
if __name__ == '__main__':
    
    PATH = 'D:\Projects\python projects\classBOT\chromedriver.exe'
    driver = uc.Chrome()
      
    data = json.load(open('tt.json'))
    monday_time = data['monday']
    tuesday_time = data['tuesday']
    wednesday_time = data['wednesday']
    thursday_time = data['thursday']
    friday_time = data['friday']
    saturday_time = data['saturday']
    sunday_time = data['sunday']
    
    schedule.every().monday.at(str(monday_time)).do(job)
    schedule.every().tuesday.at(str(tuesday_time)).do(job)
    schedule.every().wednesday.at(str(wednesday_time)).do(job)
    schedule.every().thursday.at(str(thursday_time)).do(job)
    schedule.every().friday.at(str(friday_time)).do(job)
    schedule.every().saturday.at(str(saturday_time)).do(job)
    schedule.every().sunday.at(str(sunday_time)).do(job)
    
    while True:
        schedule.run_pending()
        sleep(1)
    
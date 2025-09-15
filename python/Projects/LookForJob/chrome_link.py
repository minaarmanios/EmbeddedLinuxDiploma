import subprocess
import webbrowser
import shutil
from selenium import webdriver
import pyautogui
import time

class ChromeLink: 
    def __init__(self,chrome_path):
        self.FAVOURITE_LINKS = {
            "facebook":"https://www.facebook.com",
            "youtube":"https://www.youtube.com",
            "github":"https://www.github.com",
            "reddit":"https://www.reddit.com"
        }
        self.chrome_browser = webbrowser.Chrome(chrome_path)
        #self.chrome_browser = webdriver.Chrome()

    def show_favourite_menu(self):
        for link in self.FAVOURITE_LINKS:
            print(link)
        return self.FAVOURITE_LINKS

    def chrome(self,url):
        self.chrome_browser.open_new(url)
        time.sleep(5)
        #switch to fullscreen
        pyautogui.press('f11')
                
                

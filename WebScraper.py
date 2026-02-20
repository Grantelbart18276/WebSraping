from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import os
import dotenv
from dotenv import load_dotenv
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import selenium
import webbrowser

import os
from dotenv import load_dotenv

class StoreData():
    def __init__(self):
        self.deviant_username_ = os.getenv("Deviant_username")
        self.deviant_password_ = os.getenv("Deviant_password")
        
        self.blender_market_username_ = os.getenv("blender_market_username")
        self.blender_market_password_ = os.getenv("blender_market_password")
        
        self.github_username_ = os.getenv("github_username")
        self.github_password_ = os.getenv("github_password")
        
        self.artstation_username_ = os.getenv("artstation_username")
        self.artstation_password_ = os.getenv("artstation_password")
        
        self.pinterest_username = os.getenv("pixiv_username")
        self.pinterest_password = os.getenv("pixiv_password")
        
        self.rr = os.getenv("rr_search")
        self.rr_username = os.getenv("rr_login_name")
        self.rr_password = os.getenv("rr_password_login")
        
        self.pxvi = os.getenv("pivi")
        self.pv_username = os.getenv("pv_username__")
        self.pv_password = os.getenv("pv_password__")


class GetLinks():
    def __init__(self):
        self.webDriver = webdriver.Firefox()
        self.driverHandles = self.webDriver.window_handles
        self.allLinks = []
        self.debugPath = r"/run/media/drdrakken/Elements/Sonstiges/Programmieren/Machine Learning/Part 13 - ProjectFolder/NamePlaceHolder/Data/ChomeDebugPath/"
        self.currentTab = self.webDriver.current_window_handle

    def Iterate2(self):
        for windows in self.driverHandles:
            current = self.webDriver.switch_to.window(windows)
            print(current)

    def Iterate(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option('debuggerAddress', 'localhost:9014')
        
        driver = webdriver.Chrome(options=options)
    
        print(driver.current_url)

class Scrape():
    load_dotenv()
    def __init__(self):
        self.textFilePath = r"/run/media/drdrakken/Elements/Sonstiges/Programmieren/Machine Learning/Part 13 - ProjectFolder/Debug/"
        self.path = "https://de.pinterest.com/login/"
        self.driver = webdriver.Firefox()

        self.deviant_username_ = os.getenv("Deviant_username")
        self.deviant_password_ = os.getenv("Deviant_password")
        
        self.blender_market_username_ = os.getenv("blender_market_username")
        self.blender_market_password_ = os.getenv("blender_market_password")
        
        self.github_username_ = os.getenv("github_username")
        self.github_password_ = os.getenv("github_password")
        
        self.artstation_username_ = os.getenv("artstation_username")
        self.artstation_password_ = os.getenv("artstation_password")
        
        self.pinterest_username = os.getenv("pixiv_username")
        self.pinterest_password = os.getenv("pixiv_password")
        
        self.rr = os.getenv("rr_search")
        self.rr_username = os.getenv("rr_login_name")
        self.rr_password = os.getenv("rr_password_login")
        
        self.pxvi = os.getenv("pivi")
        self.pv_username = os.getenv("pv_username__")
        self.pv_password = os.getenv("pv_password__")
        
    def AutoCorrectString(self , String : str):
            return String.replace(" ",  ".")
    
    def OpenPages(self , Page : str = None):
        if not Page:
            page = str(r"https://en.wikipedia.org/wiki/World_War_II")
        try:
            self.driver.get(page)

            searchTextElements = self.driver.find_elements(By.XPATH , "//p")
            all_texts = [elem.text for elem in searchTextElements]

            internetText = []

            for text in all_texts:
                internetText.append(text)

            self.driver.close()
            textFilePath = os.path.join(self.textFilePath + "LLMLanguageText")
            with open(textFilePath , mode= "w" , encoding= "utf-8") as tF:
                full_text = "\n".join(internetText)
                tF.write(full_text)
                
                print(f"Erfolgreich geschrieben! Zeichenanzahl: {len(full_text)}")

        except Exception as e:
            print(e)
            return
        
exe = Scrape()
exe.OpenPages()
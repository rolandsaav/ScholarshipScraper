from lib2to3.pgen2 import driver
import time
from bs4 import BeautifulSoup as soup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class Scholarship:
    def __init__(self, _name, _desc) -> None:
        self.name = _name
        self.desc = _desc


currentpage = 1
keepRunning = True
scholarships = []

driver = webdriver.Chrome()
driver.get('https://scholarshipamerica.org/students/browse-scholarships/')

mainDiv = driver.find_element(By.CLASS_NAME, 'facetwp-template')
articles = mainDiv.find_elements(By.TAG_NAME, 'article')

info = articles[0].find_element(By.CLASS_NAME, 'info')

articles[0].find_element(By.CLASS_NAME, 'more').click()

time.sleep(0.5)

print(info.text)

driver.close()

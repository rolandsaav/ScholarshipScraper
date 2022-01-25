import time
from bs4 import BeautifulSoup as soup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class Scholarship:
    def __init__(self, _name, _desc) -> None:
        self.name = _name
        self.desc = _desc


currentpage = 1
keepRunning = True
scholarships = []

driver = webdriver.Chrome()
driver.get('https://scholarshipamerica.org/students/browse-scholarships/')


while(keepRunning):
    time.sleep(1)
    mainDiv = driver.find_element(By.CLASS_NAME, 'facetwp-template')
    articles = mainDiv.find_elements(By.TAG_NAME, 'article')

    for ele in articles:
        actions = ActionChains(driver)
        actions.move_to_element(ele).perform()
        button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, 'more')))
        button.click()

    time.sleep(0.5)

    for ele in articles:
        name = ele.find_element(By.TAG_NAME, 'h3').text
        desc = ele.find_element(By.CLASS_NAME, 'info').text

        scholarships.append(Scholarship(name, desc))

    pageButtons = driver.find_element(
        By.CLASS_NAME, 'facetwp-pager').find_elements(By.TAG_NAME, 'a')

    maxPage = -1
    nextPageButton = None

    for button in pageButtons:
        if button.get_dom_attribute('data-page') == None or button.get_dom_attribute('data-page') == "None":
            continue

        pageNum = int(button.get_dom_attribute('data-page'))

        if pageNum > maxPage:
            maxPage = pageNum

        if pageNum == currentpage + 1:
            nextPageButton = button

    if(currentpage == maxPage):
        keepRunning = False

    currentpage = currentpage + 1

    if(nextPageButton != None):
        nextPageButton.click()
    else:
        break

with open("scholarships.txt", "w") as f:
    for s in scholarships:
        f.write(s.name + "\n" + s.desc + "\n\n")

driver.close()

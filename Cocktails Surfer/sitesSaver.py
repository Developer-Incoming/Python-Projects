from selenium import webdriver
from selenium.webdriver.common.by import By

import numpy as np

# from bs4 import BeautifulSoup

cdPath = "D:\chromedriver\chromedriver.exe"
driver = webdriver.Chrome(executable_path=cdPath)

# nextCocktailButton = driver.find_element_by_class_name("btn btn-block btn-sm btn-success")
# nextCocktailButton.click()
# .getElementsByClassName("col-12 btn shadow-sm mb-2 text-left")[0].href
# document.querySelector("#swipeme > div:nth-child(3) > div:nth-child(2) > div.row.justify-content-sm-center > div:nth-child(1)")
# driver.find_element(By.CLASS_NAME, "")

cocktailsPages = open("D:\path\Cocktails Surfer\completeCocktailLinks.txt", "r").read().split("\n")

def openPage(url):
    driver.get(url)

def savePage(pageSpecialName):
    # print("yas, save page")

    # driver.find_element(By.CSS_SELECTOR, "head > link:nth-child(42)")[0].setAttribute("href", "css.css?v=20229")
    driver.execute_script("arguments[0].setAttribute('href',arguments[1])", driver.find_element(By.CSS_SELECTOR, "head > link:nth-child(42)"), "css.css?v=20229")
    content = driver.page_source
    # print(content)

    # soup = BeautifulSoup(content)
    file = open("D:\path\Cocktails Surfer\Cocktails Pages\\" + pageSpecialName + ".html", "w", encoding="utf-8")
    file.write(content)

def main():
    for pageLink in cocktailsPages[3346:]:
        openPage(pageLink)
        savePage(pageLink.split("/")[5])
    

main()

driver.close()

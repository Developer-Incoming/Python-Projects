from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

cdPath = "D:\chromedriver\chromedriver.exe"
driver = webdriver.Chrome(executable_path=cdPath)

# nextCocktailButton = driver.find_element_by_class_name("btn btn-block btn-sm btn-success")
# nextCocktailButton.click()
# .getElementsByClassName("col-12 btn shadow-sm mb-2 text-left")[0].href
# document.querySelector("#swipeme > div:nth-child(3) > div:nth-child(2) > div.row.justify-content-sm-center > div:nth-child(1)")
# driver.find_element(By.CLASS_NAME, "")

cocktailLinksFile = open("D:\path\Cocktails Surfer\cocktailLinks.txt", "w")
cocktailsPages = open("D:\path\Cocktails Surfer\yay.txt", "r").read().split("\n")

def openPage(url):
    driver.get(url)

def getCocktailsInPage():
    cocktailsLinksFound = []
    cocktailsList = driver.find_elements(By.TAG_NAME, "a")

    for i in range(1,19):
        # print(cocktailsList[i].get_attribute("href"))
        cocktailsLinksFound.append(cocktailsList[i].get_attribute("href"))
    
    cocktailsLinksFound.append("\n")
    return cocktailsLinksFound

def appendCocktailsFound():
    cocktailLinksFile.writelines("\n".join(getCocktailsInPage()))
    cocktailLinksFile.write("\n")

def main():
    for pageLink in cocktailsPages:
        openPage(pageLink)
        appendCocktailsFound()
    

main()

cocktailLinksFile.close()

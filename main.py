
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support import expected_conditions as EC


def main():
    driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

    driver.get("https://www.dlsite.com/home/work/=/product_id/RJ260395.html")
    wait = WebDriverWait(driver, 10)
    element_locator = ("xpath", '/html/body/div[3]/div/ul/li[2]/a')
    element = wait.until(EC.visibility_of_element_located(element_locator))
    element.click()

    table = driver.find_element("id","work_outline")
    print(table.text)
    colpath = "/html/body/div[3]/div[4]/div[1]/div/div[1]/div[2]/div[2]/table/tbody/tr[1]/th"
    rowpath = "/html/body/div[3]/div[4]/div[1]/div/div[1]/div[2]/div[2]/table/tbody/tr[1]"
    cols = 1+len(driver.find_elements("xpath",colpath))

    rows = len(driver.find_elements("xpath",rowpath))
    tags = []
    for r in range(1, 13):  
        th = driver.find_element("xpath", 
            "/html/body/div[3]/div[4]/div[1]/div/div[1]/div[2]/div[2]/table/tbody/tr["+str(r)+"]/th[1]").text
        value = driver.find_element("xpath", 
            "/html/body/div[3]/div[4]/div[1]/div/div[1]/div[2]/div[2]/table/tbody/tr["+str(r)+"]/td[1]").text
        tags.append(str(th+": "+value+"   "))
    print(tags)

    f = open ("RJtest.txt",'a',encoding="utf-8")
    for i in tags:
        f.write(i+"\n")

    f.close()

if __name__ = "__main__":
    main()
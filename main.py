# selenium 4
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options
from selenium.webdriver import Firefox

# cli.py
import click


def get_metadata(driver):
    table = driver.find_element("id","work_outline")
    colpath = "/html/body/div[3]/div[4]/div[1]/div/div[1]/div[2]/div[2]/table/tbody/tr[1]/th"
    rowpath = "/html/body/div[3]/div[4]/div[1]/div/div[1]/div[2]/div[2]/table/tbody/tr[1]"
    cols = 1+len(driver.find_elements("xpath",colpath))

    rows = len(driver.find_elements("xpath",rowpath))
    result = []
    for r in range(1, 13):  
        th = driver.find_element("xpath", 
            "/html/body/div[3]/div[4]/div[1]/div/div[1]/div[2]/div[2]/table/tbody/tr["+str(r)+"]/th[1]").text
        td = driver.find_element("xpath", 
            "/html/body/div[3]/div[4]/div[1]/div/div[1]/div[2]/div[2]/table/tbody/tr["+str(r)+"]/td[1]").text
        result.append(str(th+": "+td+"   "))
    return result

def get_thumbnail(driver):
    path = "/html/body/div[3]/div[4]/div[1]/div/div[1]/div[1]/div/div/div[2]/div/div/div/ul/li/picture/img"
    result = "<img src=\"https://"+str(driver.find_elements("xpath",path)[0].get_attribute("outerHTML").split(' ')[1][:-1][10:])+"\"> "
    #print(result)
    return result

@click.command()
@click.argument('rjcode')
def main(rjcode):
    if rjcode == "":
        return
    else:
        options = Options()
        options.add_argument("--headless")
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()),options=options)

        driver.get(f"https://www.dlsite.com/home/work/=/product_id/{rjcode}.html")
        wait = WebDriverWait(driver, 10)
        element_locator = ("xpath", '/html/body/div[3]/div/ul/li[2]/a')
        element = wait.until(EC.visibility_of_element_located(element_locator))
        element.click()
        metadata=get_metadata(driver)

        f = open (f"./{rjcode}.md",'a',encoding="utf-8")

        for i in metadata:
            f.write(i+"\n")
        f.write(get_thumbnail(driver))
        f.close()
        driver.quit()

if __name__ == "__main__":
    main()
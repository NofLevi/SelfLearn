import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

class Functions:
    
    def title_and_source():
        choice = input("Title and SourceCode Options:\n1.KSP [Default]\n2.Custom")
        if(1):
            driver = webdriver.Chrome() #set webdriver
            driver.maximize_window()
            driver.get("https://ksp.co.il/web/")
            print("Page title is: " + driver.title)
            print(driver.page_source)#get pagesource

            time.sleep(5)
            driver.quit();
        else:
            site = input("Enter the site you want:")
            driver = webdriver.Chrome()
            driver.maximize_window()
            driver.get(site)
            print("Page title is: " + driver.title)
            print(driver.page_source)#get pagesource

            time.sleep(5)
            driver.quit();

    def locators():
        print("BMI Calculator [Locators Example]:")
        userage = input("Enter age: ")
        userheight = input("Enter Height: ")
        userweight = input("Enter Weight: ")
        driver = webdriver.Chrome()
        driver.fullscreen_window
        driver.get("https://www.calculator.net/bmi-calculator.html")
        age = driver.find_element_by_id("cage")#find element by id
        height = driver.find_element_by_id("cheightmeter")
        weight = driver.find_element_by_name("ckg") #find element by name
        button = driver.find_element_by_css_selector("#content > div.leftinput > div.panel2 > table > tbody > tr > td > table:nth-child(4) > tbody > tr > td > input[type=image]:nth-child(2")

        try:
            age.clear()
            age.send_keys(userage)
            time.sleep(1)

            height.clear()
            height.send_keys(userheight)
            time.sleep(1)

            weight.clear()
            weight.send_keys(userweight)
            time.sleep(1)

        except:
            print("Enter Keys failed")

        button.click()
        
        time.sleep(5)
        driver.quit();

    def drop_down_menu():
            driver = webdriver.Chrome() #set webdriver
            driver.maximize_window()
            driver.get("http://echoecho.com/htmlforms11.htm")

            try:
                time.sleep(1)
                sel = Select(driver.find_element_by_name("dropdownmenu"))
                sel.select_by_visible_text("Milk")
            
            except Exception as e:
                print(e)
            time.sleep(5)
            driver.quit();
            

    def verification():
            driver = webdriver.Chrome() #set webdriver
            driver.maximize_window()
            driver.get("https://flyff-iblis.com/index.php")
            #putting id and password then clicking on the confirmbutton

            try:
                driver.find_element_by_name("username").send_keys("testtest123")
                driver.find_element_by_name("password").send_keys("testtest123")
                driver.find_element_by_css_selector("body > div.bgwrap > div > div.bgfrontwrap > div > div > div.bg-content.shadow > div.column-left > div:nth-child(1) > div.inner-content.text-center > form > button").click()

                #checking if verification pass
                logged = driver.find_element_by_css_selector("body > div.bgwrap > div > div.bgfrontwrap > div > div > div.bg-content.shadow > div.column-left > div:nth-child(1) > div.inner-content-logged.text-center > a:nth-child(6) ")
                displayed = logged.is_displayed()

                if displayed:
                    print("Element was displayed")
                else:
                    print("Element wasnt displayed")

                time.sleep(5)
                driver.quit();
            except Exception as e:
                print(e)
        
        
                         
            
            
              





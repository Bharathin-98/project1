from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class orangehrm():

  def test(self):
    driver= webdriver.Firefox() # opens the browser
    url="https://opensource-demo.orangehrmlive.com/web/index.php/auth/login" # opens the orange hrm page
    driver.get(url)
    driver.maximize_window() # maximize the window
    time.sleep(5)

    #Testcase-2:login with correct user name and  incorrect password

  # xpath for user name
    xpath_to_userinputbox="//input[@name='username']"
    search_box=driver.find_element(By.XPATH,xpath_to_userinputbox)
    search_box.send_keys("Admin")
    search_box.send_keys(Keys.ENTER)

  # xpath for password
    xpath_to_passwordinputbox="//input[@type='password']"
    search_box=driver.find_element(By.XPATH,xpath_to_passwordinputbox)
    search_box.send_keys("admin124")
    search_box.send_keys(Keys.ENTER)
    time.sleep(5)
    print("The user not login sucessfully")
    time.sleep(3)
    driver.quit()

ab=orangehrm()
ab.test()

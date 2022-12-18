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

  #Testcase-1:login with correct user name and password

  # xpath for user name
    xpath_to_userinputbox="//input[@name='username']"
    search_box=driver.find_element(By.XPATH,xpath_to_userinputbox)
    search_box.send_keys("Admin")
    search_box.send_keys(Keys.ENTER)

  # xpath for password
    xpath_to_passwordinputbox="//input[@type='password']"
    search_box=driver.find_element(By.XPATH,xpath_to_passwordinputbox)
    search_box.send_keys("admin123")
    search_box.send_keys(Keys.ENTER)
    time.sleep(5)
    print("The user login sucessfully")
    time.sleep(3)

    #Test_pim01
    xpath_to_Pim="//a[@href='/web/index.php/pim/viewPimModule']"
    enter_pim = driver.find_element(By.XPATH,xpath_to_Pim)
    enter_pim.click()
    time.sleep(3)

    xpath_to_addbutton="//button[@class='oxd-button oxd-button--medium oxd-button--secondary']"
    add_button_element=driver.find_element(By.XPATH,xpath_to_addbutton)
    add_button_element.click()
    time.sleep(3)
    #Adding user details
    xpath_to_firstname="//input[@name='firstName']"
    first_name=driver.find_element(By.XPATH,xpath_to_firstname)
    first_name.send_keys("Bharathi")
    time.sleep(3)
    xpath_to_middlename="//input[@name='middleName']"
    middle_name=driver.find_element(By.XPATH,xpath_to_middlename)
    middle_name.send_keys("Nagarajan Kalyani")
    time.sleep(3)
    xpath_to_lastname="//input[@name='lastName']"
    last_name=driver.find_element(By.XPATH,xpath_to_lastname)
    last_name.send_keys("N")
    time.sleep(3)

    xpath_to_save="//button[@type='submit']"
    save=driver.find_element(By.XPATH,xpath_to_save)
    save.click()
    time.sleep(5)
  
    
    print("Details saved successfully")
    time.sleep(3)
    
    driver.close()
  
ab=orangehrm()
ab.test()

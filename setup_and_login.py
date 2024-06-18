from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import (ElementNotVisibleException, ElementNotSelectableException)
from selenium.webdriver.support.ui import WebDriverWait
# import simulate_input as input
import time
# import main
from dotenv import load_dotenv
import os
from selenium.webdriver.common.by import By

# Load environment variables from .env file
load_dotenv()

def driver_setup():

    # Set up Chrome options to use the existing profile
    chrome_options = Options()
    chrome_profile = r'C:\Users\se_ba\AppData\Local\Google\Chrome\User Data'  # Change this path to your profile path
    chrome_options.add_argument(f"user-data-dir={chrome_profile}")
    chrome_options.add_argument("profile-directory=Default")  # Name of the profile directory

    # Specify the path to the Chrome executable if it is not in the default location
    chrome_options.binary_location = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"

    # chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("detach", True)  # TODO: Modify as needed for debug mode
    driver = webdriver.Chrome(options=chrome_options)    

    # options = webdriver.ChromeOptions()
    # options.add_experimental_option("detach", True)  # TODO: Modify as needed for debug mode
    # driver = webdriver.Chrome(options=options)    

    # Makes driver wait 10 seconds before throwing an exception
    driver.implicitly_wait(10)

    # create action chain object
    action = ActionChains(driver)

    ignore_list = [ElementNotVisibleException, ElementNotSelectableException]
    wait = WebDriverWait(driver, timeout=10, poll_frequency=1, ignored_exceptions=ignore_list)
    return driver, action, wait
    
def login(driver, action, wait):
    # Username and password
    username_field = driver.find_element(By.NAME, 'Email')
    password_field = driver.find_element(By.NAME, 'password')
    username_field.send_keys(os.getenv('EMAIL'))
    time.sleep(2)
    password_field.send_keys(os.getenv('PASSWORD'))
    password_field.send_keys(Keys.RETURN)
    # input.slow_type(driver.find_element('xpath', '//*[@id="ap_email"]'), os.getenv('EMAIL'))

    # Password
    # input.slow_type(driver.find_element('xpath', '//*[@id="ap_password"]'), os.getenv('PASSWORD'))

    # Sign in button
    # input.element_click(driver, action, wait, '//*[@id="signInSubmit"]')



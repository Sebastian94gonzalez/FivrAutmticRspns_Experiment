import setup_and_login as snl
import simulate_input as input
from selenium.webdriver.chrome.options import Options
import time


driver, actions, wait = snl.driver_setup()

url = 'https://www.fiverr.com/login'
driver.get(url)
time.sleep(10)
# input.element_click(driver, actions, wait, '//*[@id="__ZONE__main"]/div/div/div/div/div/div/section/div/div[2]/section/section[1]/button[1]/p')
time.sleep(13)
# Locate the "Press & Hold" button
##button = driver.find_element_by_xpath('//button[contains(text(), "Press ")]')

# Perform a long press (click and hold)
##actions.click_and_hold(button).perform()

# Hold the button for the required duration
##time.sleep(5)  # Adjust the duration as necessary

# Release the button
##actions.release().perform()

# Wait for the next page or action to complete
##time.sleep(5)

# input.element_click(driver, action, wait, '//*[@id="pQRKZKZbfDrOEgt"]')


# snl.login(driver, actions, wait)
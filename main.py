import setup_and_login as snl
import simulate_input as input
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import re


def captchaCheck():
    
    pass

driver, actions, wait = snl.driver_setup()
time.sleep(1)
url = 'https://www.fiverr.com'
driver.get(url)
print(driver.find_element(By.CSS_SELECTOR,'#px-captcha'))
# element = driver.find_element(By.CSS_SELECTOR,'#px-captcha')
element = driver.find_element(By.XPATH,'/html/body/div/div/div[2]/div[2]/p')
print(element.get_attribute('innerHTML'))
actions.click_and_hold(element)
actions.perform()
time.sleep(1)
notFinished = True

articleElement = driver.find_element(By.TAG_NAME, 'article')
print('articleElement\n' + str(articleElement))
styleElements = driver.find_elements(By.TAG_NAME, 'style')
print('styleElements\n' + str(styleElements))
styles_test = driver.find_elements(By.XPATH, '/html/head/style')

print('styles_test\n' + str(styles_test))

class_pattern = re.compile(r'pointer\}(.*?)\{')

# for style in styleElements:
#     style_text = style.get_attribute('innerHTML')
#     print(style_text)
#     matches = class_pattern.findall(style_text)
#     for match in matches:
#         print(f"Extracted text: {match}")
    # if class_pattern.match(style.get_attribute('body')):
    #     continue

# while (notFinished):
#     articleElement = driver.find_element(By.TAG_NAME, '<article>')
#     styleElements = driver.find_element(By.TAG_NAME, '<style>')
#     styles_test = driver.find_elements(By.XPATH, '/html/head/style')
#     pass

time.sleep(10)
actions.release(element)
actions.perform()
time.sleep(0.2)
actions.release(element)
# input.element_click(driver, actions, wait, '//*[@id="__ZONE__main"]/div/div/div/div/div/div/section/div/div[2]/section/section[1]/button[1]/p')
# time.sleep(13)
# Locate the "Press & Hold" button
##button = driver.find_element(By.XPATH,'//button[contains(text(), "Press ")]')

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
from seleniumbase import SB
from dotenv import load_dotenv
from selenium.webdriver.chrome.options import Options
import pyautogui
import os

# Load environment variables from .env file
load_dotenv(r'C:\Users\se_ba\Desktop\PyProjects\FivrAutmticRspns_Experiment\env_vars.env')
# load_dotenv()

# user_data_dir=r'C:\Users\se_ba\AppData\Local\Google\Chrome\User Data\Default'
with SB(uc=True) as sb:
    # options = Options()
    # options = sb.get_new_driver_options()
    # options.add_argument(r'user-data-dir=C:\Users\se_ba\AppData\Local\Google\Chrome\User Data')
    # options.add_argument(r"profile-directory=Default")  # Change to your profile directory if necessary
    # sb.driver.get_new_driver(options=options)   # Big question mark on this line

    # sb.driver = sb.get_new_driver(options=options)
    # sb.driver = sb.get_new_driver(options)

    url = 'https://www.fiverr.com'
    sb.driver.get(url)
    sb.sleep(1)
    # sb.click('a:contains("Sign in")')
    sb.click_xpath('//*[@id="Header"]/header/div/div/nav/ul/li[5]/a')
    sb.sleep(1)
    try: 
        selector = 'body > div.modal-package.ppc6UJV.user-session-package.user_session-package.signing-modal.identification-modal.standard.QSUsfqZ > div > section > div > section > div > div.MItej_K > section > section.T3SWCUH > button.GfxqusN.rxnFpuj.sEPVjjj.icon-button.social-signing-button.google-signing-button.YCx8BDM > p'
        sb.click_visible_elements(selector, by="css selector", limit=0, timeout=None)
    except:
        # sb.click_xpath('/html/body/div[19]/div/section/div/section/div/div[2]/section/section[1]/button[1]/p')
        sb.click_xpath('/html/body/div[26]/div/section/div/section/div/div[2]/section/section[1]/button[1]/p')
    sb.sleep(1)
    username_field = str(os.getenv('EMAIL'))
    password_field = str(os.getenv('PASSWORD'))
    sb.send_keys('#identifierId', username_field, by='css selector')
    sb.sleep(1)
    sb.click_xpath('//*[@id="identifierNext"]/div/button/span')
    sb.sleep(2)
    sb.send_keys('#password > div.aCsJod.oJeWuf > div > div.Xb9hP > input', password_field, by='css selector')
    sb.click_xpath('//*[@id="passwordNext"]/div/button/span')
    sb.sleep(1)
    selector = '#yDmH0d > c-wiz > div > div.UXFQgc > div > div > div > form > span > section:nth-child(2) > div > div > section > div > div > div > ul > li:nth-child(4) > div > div.l5PPKe'
    sb.click_visible_elements(selector, by="css selector", limit=0, timeout=None)
    sb.sleep(1)
    selector = '#yDmH0d > c-wiz > div > div.JYXaTc > div > div.TNTaPb > div > div > button > span'
    sb.click_visible_elements(selector, by="css selector", limit=0, timeout=None)
    
    sb.sleep(1)
    # Type PIN
    pyautogui.typewrite(str(os.getenv('PASSKEY')))
    
    # Press enter
    pyautogui.press('enter')

    sb.sleep(5)
    sb.click_xpath('//*[@id="Header"]/header/div/div/nav/ul/li[3]/div/div/span/div/span/button/span/svg')
    sb.sleep(1)
    selector = 'body > div:nth-child(153) > aside > div > section > footer > a.view-all'
    sb.click_visible_elements(selector, by="css selector", limit=0, timeout=None)

    # TODO: MFA is triggering and so this introduces an issue. How to avoid, or how to turn off MFA
        # - If not, can I log into the existing profile using seleniumbase? -> Could not
        # - Can the pass key functionality work with a script that handles the Windows Security 
        #   PassKey functionality?
    
    sb.sleep(1)
    # username_field.send_keys(os.getenv('EMAIL'))
    # time.sleep(2)
    # password_field.send_keys(os.getenv('PASSWORD'))
    # password_field.send_keys(Keys.RETURN)
from seleniumbase import SB
from dotenv import load_dotenv
import os
import pyautogui


# Load environment variables from .env file
load_dotenv(r'C:\Users\se_ba\Desktop\PyProjects\FivrAutmticRspns_Experiment\env_vars.env')
# load_dotenv()

# user_data_dir=r'C:\Users\se_ba\AppData\Local\Google\Chrome\User Data\Default'
with SB(uc=True) as sb:
    url = 'https://www.fiverr.com'
    sb.driver.get(url)
    sb.sleep(1)
    # sb.click('a:contains("Sign in")')
    sb.click_xpath('//*[@id="Header"]/header/div/div/nav/ul/li[5]/a')
    sb.sleep(1)
    # Continue with email/username
    selector = 'body > div.modal-package.ppc6UJV.user-session-package.user_session-package.signing-modal.identification-modal.standard.QSUsfqZ > div > section > div > section > div > div.MItej_K > section > section.T3SWCUH > button.GfxqusN.rxnFpuj.sEPVjjj.icon-button.tZeeQ0r > p'
    sb.click_visible_elements(selector, by="css selector", limit=0, timeout=None)
    sb.sleep(1)
    username_field = str(os.getenv('EMAIL'))
    password_field = str(os.getenv('PASSWORD'))
    sb.send_keys('#login', username_field, by='css selector')
    sb.sleep(1)
    sb.send_keys('#password', password_field, by='css selector')
    # Sign in enter button
    selector = 'body > div.modal-package.ppc6UJV.user-session-package.user_session-package.signing-modal.identification-modal.standard.QSUsfqZ > div > section > div > section > div > div.MItej_K > form > section > section.flex.flex-col.flex-justify-end.FXwNHmU.eMGf4JM > button'
    sb.click_visible_elements(selector, by="css selector", limit=0, timeout=None)
    sb.sleep(1)
    # Mailbox icon at landing page TODO: Potentially diffrent selector variable on seller account
    selector = '#Header > header > div > div > nav > ul > li.display-from-md.Gufp02I.EfViiAm > div > div > span > div > span > button > span > svg > path:nth-child(2)'
    sb.click_visible_elements(selector, by="css selector", limit=0, timeout=None)
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
    sb.sleep(3)
    # sb.switch_to_window(0)
    sb.switch_to_default_window()
    # sb.open_new_window(switch_to=True)
    sb.click_xpath('//*[@id="Header"]/header/div/div/nav/ul/li[3]/div/div/span/div/span/button/span/svg/path[2]')
    sb.sleep(1)
    selector = 'body > div:nth-child(153) > aside > div > section > footer > a.view-all'
    sb.click_visible_elements(selector, by="css selector", limit=0, timeout=None)

    # TODO: Separate login from windows security key through google SSO. 
        # May need to re-configure Fiverr settings

    sb.sleep(1)
    # username_field.send_keys(os.getenv('EMAIL'))
    # time.sleep(2)
    # password_field.send_keys(os.getenv('PASSWORD'))
    # password_field.send_keys(Keys.RETURN)
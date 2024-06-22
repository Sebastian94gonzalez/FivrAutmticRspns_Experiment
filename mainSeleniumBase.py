from seleniumbase import SB
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv(r'C:\Users\se_ba\Desktop\PyProjects\FivrAutmticRspns_Experiment\env_vars.env')
# load_dotenv()


with SB(uc=True) as sb:
    url = 'https://www.fiverr.com'
    sb.driver.get(url)
    sb.sleep(1)
    # sb.click('a:contains("Sign in")')
    sb.click_xpath('//*[@id="Header"]/header/div/div/nav/ul/li[5]/a')
    sb.sleep(1)
    try: 
        sb.click_xpath('/html/body/div[27]/div/section/div/section/div/div[2]/section/section[1]/button[1]/p')
    except:
        sb.click_xpath('/html/body/div[24]/div/section/div/section/div/div[2]/section/section[1]/button[1]/p')
    sb.sleep(1)
    username_field = str(os.getenv('EMAIL'))
    password_field = str(os.getenv('PASSWORD'))
    sb.send_keys('#identifierId', username_field, by='css selector')
    sb.sleep(1)
    sb.click_xpath('//*[@id="identifierNext"]/div/button/span')
    sb.sleep(2)
    sb.send_keys('#password > div.aCsJod.oJeWuf > div > div.Xb9hP > input', password_field, by='css selector')
    
    sb.click_xpath('//*[@id="passwordNext"]/div/button/span')
    # TODO: MFA is triggering and so this introduces and issue. How to avoid, or how to turn off MFA
        # - If not, can I log into the existing profile using seleniumbase?
    
    sb.sleep(1)
    # username_field.send_keys(os.getenv('EMAIL'))
    # time.sleep(2)
    # password_field.send_keys(os.getenv('PASSWORD'))
    # password_field.send_keys(Keys.RETURN)
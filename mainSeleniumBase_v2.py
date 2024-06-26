from seleniumbase import BaseCase
from dotenv import load_dotenv
import os
import unittest

class MyTestClass(BaseCase):

    def setUp(self):
        super().setUp()
        # Specify the path to your Chrome user data directory and the profile
        options = self.get_new_driver_options()
        options.add_argument(r'user-data-dir=C:\Users\se_ba\AppData\Local\Google\Chrome\User Data')
        options.add_argument(r"profile-directory=Default")  # Change to your profile directory if necessary
        self.driver = self.get_new_driver(options)

    def test_open_chrome_with_profile(self):
        load_dotenv()
        email = os.getenv('EMAIL')
        password = os.getenv('PASSWORD')
        
        self.open("https://www.fiverr.com")
        self.type("input[name='username']", email)
        self.type("input[name='password']", password)
        self.click("button[type='submit']")

if __name__ == "__main__":
    unittest.main(argv=[''], verbosity=2, exit=False)
from django.test import LiveServerTestCase
from rest_framework.test import APIClient
from selenium import webdriver

DRIVER_PATH = r"D:\PROJECTS\geckodriver\geckodriver.exe"

URL = "http://localhost:3000/"

class TestNewUser(LiveServerTestCase):
    
    port = 8000

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.browser = webdriver.Firefox(executable_path=DRIVER_PATH)
    
    @classmethod
    def tearDownClass(cls):
        cls.browser.quit()
        super().tearDownClass()

    def test_new_user(self):
        self.browser.get(URL)

        # new user comes to website
        # user checks title 
        # user checks page contents

        # user creates new note
        # user checks if note is created

        # user creates another new note
        # user checks if note is created

        # user connects two notes
        # user checks if two notes is connected


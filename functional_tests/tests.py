import time

from django.test import LiveServerTestCase
from rest_framework.test import APIClient
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.keys import Keys

DRIVER_PATH = r"D:\PROJECTS\geckodriver\geckodriver.exe"

URL = "http://localhost:3000/"

class TestNewUser(LiveServerTestCase):
    
    port = 8000

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.browser = webdriver.Firefox(executable_path=DRIVER_PATH)
        cls.action_chains = ActionChains(cls.browser)
    
    @classmethod
    def tearDownClass(cls):
        cls.browser.quit()
        super().tearDownClass()

    def wait_for_element(self, callback):
        start_time = time.time()
        while True:
            try:
                element = callback()
                if element:
                    return element
            except (WebDriverException) as e:
                print(e)
                if time.time() - start_time > TIME_LIMIT:
                    raise e
                time.sleep(0.5)

    def test_new_user(self):

        # new user comes to website
        # user checks title 
        # user checks page contents
        self.browser.get(URL)
        self.assertEqual("Crime Board", self.browser.title)
        self.assertIn("Create your own crime board for fun!", self.browser.page_source)

        # user creates new note
        # user checks if note is created
        crime_board = self.browser.find_element_by_id("crime-board")
        self.action_chains.double_click(crime_board).perform()
        notes = self.wait_for_element(
            lambda: self.browser.find_elements_by_class_name("note")
        )
        self.assertEqual(len(notes), 1)

        # user creates another new note
        # user checks if note is created

        # user connects two notes
        # user checks if two notes is connected


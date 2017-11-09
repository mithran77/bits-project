import os
import ast
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.firefox.webdriver import WebDriver

TESTDATA_FILENAME = os.path.join(os.path.dirname(__file__), '../../fixtures/testdata.json')

class SeleniumTests(StaticLiveServerTestCase):

    @classmethod
    def setUpClass(cls):
        super(SeleniumTests, cls).setUpClass()
        cls.testdata = open(TESTDATA_FILENAME).read()
        cls.testdata = cls.testdata.replace('\n', '')
        cls.testdata = ast.literal_eval(cls.testdata)
        cls.selenium = WebDriver()
        cls.selenium.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super(SeleniumTests, cls).tearDownClass()

    def test_sign_up(self):
        self.selenium.get('%s%s' % (self.testdata['server_address'], '/signup/'))
        username_input = self.selenium.find_element_by_name("username")
        username_input.send_keys(self.testdata['create_user']['fields']['username'])
        first_name_input = self.selenium.find_element_by_name("first_name")
        first_name_input.send_keys(self.testdata['create_user']['fields']['first_name'])
        last_name_input = self.selenium.find_element_by_name("last_name")
        last_name_input.send_keys(self.testdata['create_user']['fields']['last_name'])
        email_input = self.selenium.find_element_by_name("email")
        email_input.send_keys(self.testdata['create_user']['fields']['email'])
        password1_input = self.selenium.find_element_by_name("password1")
        password1_input.send_keys(self.testdata['create_user']['fields']['password'])
        password2_input = self.selenium.find_element_by_name("password2")
        password2_input.send_keys(self.testdata['create_user']['fields']['password'])
        self.selenium.find_element_by_xpath('//button').click()

    def test_login(self):
        self.selenium.get('%s%s' % (self.testdata['server_address'], '/login/'))
        username_input = self.selenium.find_element_by_name("username")
        username_input.send_keys(self.testdata['created_user']['username'])
        password_input = self.selenium.find_element_by_name("password")
        password_input.send_keys(self.testdata['created_user']['password'])
        self.selenium.find_element_by_xpath('//button').click()

    def test_logout(self):
        self.selenium.get('%s%s' % (self.testdata['server_address'], '/login/'))
        username_input = self.selenium.find_element_by_name("username")
        username_input.send_keys(self.testdata['created_user']['username'])
        password_input = self.selenium.find_element_by_name("password")
        password_input.send_keys(self.testdata['created_user']['password'])
        self.selenium.find_element_by_xpath('//button').click()		
        self.selenium.find_element_by_xpath('/html/body/div[2]/div/span[2]/a').click()


	def test_caterer_select(self):
		# Login
        self.selenium.get('%s%s' % (self.testdata['server_address'], '/login/'))
        username_input = self.selenium.find_element_by_name("username")
        username_input.send_keys(self.testdata['created_user']['username'])
        password_input = self.selenium.find_element_by_name("password")
        password_input.send_keys(self.testdata['created_user']['password'])
        self.selenium.find_element_by_xpath('//button').click()

		# Navigate to caterer detail
		

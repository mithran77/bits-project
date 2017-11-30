import os
import ast
import time
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common import action_chains, keys
from selenium.common.exceptions import StaleElementReferenceException
from commonfns import TestHelper

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
        self.helper = TestHelper()

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super(SeleniumTests, cls).tearDownClass()

    def test_sign_up_existing_user(self):
        self.selenium.get('%s%s' % (self.testdata['server_address'], '/signup/'))
        username_input = self.selenium.find_element_by_name("username")
        username_input.send_keys(self.testdata['existing_user']['fields']['username'])
        first_name_input = self.selenium.find_element_by_name("first_name")
        first_name_input.send_keys(self.testdata['existing_user']['fields']['first_name'])
        last_name_input = self.selenium.find_element_by_name("last_name")
        last_name_input.send_keys(self.testdata['existing_user']['fields']['last_name'])
        email_input = self.selenium.find_element_by_name("email")
        email_input.send_keys(self.testdata['existing_user']['fields']['email'])
        password1_input = self.selenium.find_element_by_name("password1")
        password1_input.send_keys(self.testdata['existing_user']['fields']['password'])
        password2_input = self.selenium.find_element_by_name("password2")
        password2_input.send_keys(self.testdata['existing_user']['fields']['password'])
        self.selenium.find_element_by_xpath('//button').click()
        error_message = self.selenium.find_element_by_xpath('/html/body/form/p[2]')
        self.assertEqual(error_message.text, 'A user with that username already exists.')
        self.assertEqual('%s%s' % (self.testdata['server_address'], '/signup/'), self.selenium.current_url)

    def test_sign_up_new_user(self):
        self.selenium.get('%s%s' % (self.testdata['server_address'], '/signup/'))
        username_input = self.selenium.find_element_by_name("username")
        username_input.send_keys(self.testdata['new_user']['fields']['username'])
        first_name_input = self.selenium.find_element_by_name("first_name")
        first_name_input.send_keys(self.testdata['new_user']['fields']['first_name'])
        last_name_input = self.selenium.find_element_by_name("last_name")
        last_name_input.send_keys(self.testdata['new_user']['fields']['last_name'])
        email_input = self.selenium.find_element_by_name("email")
        email_input.send_keys(self.testdata['new_user']['fields']['email'])
        password1_input = self.selenium.find_element_by_name("password1")
        password1_input.send_keys(self.testdata['new_user']['fields']['password'])
        password2_input = self.selenium.find_element_by_name("password2")
        password2_input.send_keys(self.testdata['new_user']['fields']['password'])
        self.selenium.find_element_by_xpath('//button').click()
        self.assertEqual('%s%s' % (self.testdata['server_address'], '/weddingServices/'), self.selenium.current_url)


    def test_login(self):
        self.helper.login()
        self.assertEqual('%s%s' % (self.testdata['server_address'], '/weddingServices/'), self.selenium.current_url)

    def test_logout(self):
        # Login
        self.helper.login()
        self.assertEqual('%s%s' % (self.testdata['server_address'], '/weddingServices/'), self.selenium.current_url)

        # Logout
        self.selenium.find_element_by_xpath('/html/body/div[2]/div/span[2]/a').click()
        self.assertEqual('%s%s' % (self.testdata['server_address'], '/weddingServices/'), self.selenium.current_url)


    def test_caterer_successful_book(self):
        # Login
        self.helper.login()

        # Navigate to caterer list
        self.selenium.find_element_by_xpath('/html/body/div[1]/a[2]').click()
        # Navigate to caterer detail
        self.selenium.find_element_by_xpath('/html/body/div[2]/div/div/div[3]/h3/a').click()
        # Navigate to caterer booking
        self.selenium.find_element_by_xpath('/html/body/div[2]/div/div/a').click()
        # Select month from drop down
        self.selenium.find_element_by_xpath("//*[@id='id_booking_date_month']/option[text()='January']").click()
        # Select day from drop down
        self.selenium.find_element_by_xpath("//*[@id='id_booking_date_day']/option[text()='1']").click()
        # Select year from drop down
        self.selenium.find_element_by_xpath("//*[@id='id_booking_date_year']/option[text()='2018']").click()
        # Select time slot AN
        self.selenium.find_element_by_xpath("//*[@id='id_time_slots_1']").click()
        # Click book button
        self.selenium.find_element_by_xpath('/html/body/form/button').click()
        self.assertIn('http://127.0.0.1:8000/weddingServices/caterers/2/bookdate', self.selenium.current_url)
        # Click buy button
        #self.selenium.find_element_by_xpath('/html/body/form/input[13]').click()
        #time.sleep(5)
        #self.assertEqual('%s%s' % (self.testdata['server_address'], '/weddingServices/'), self.selenium.current_url)

    def test_hall_successful_book(self):
        # Login
        self.helper.login()

        # Navigate to caterer list
        self.selenium.find_element_by_xpath('/html/body/div[1]/a[1]').click()
        # Navigate to caterer detail
        self.selenium.find_element_by_xpath('/html/body/div[2]/div/div/div[3]/h3/a').click()
        # Navigate to caterer booking
        self.selenium.find_element_by_xpath('/html/body/div[2]/div/div/a').click()
        # Select month from drop down
        self.selenium.find_element_by_xpath("//*[@id='id_booking_date_month']/option[text()='January']").click()
        # Select day from drop down
        self.selenium.find_element_by_xpath("//*[@id='id_booking_date_day']/option[text()='1']").click()
        # Select year from drop down
        self.selenium.find_element_by_xpath("//*[@id='id_booking_date_year']/option[text()='2018']").click()
        # Select time slot AN
        self.selenium.find_element_by_xpath("//*[@id='id_time_slots_1']").click()
        # Click book button
        self.selenium.find_element_by_xpath('/html/body/form/button').click()
        self.assertIn('http://127.0.0.1:8000/weddingServices/halls/1/bookdate', self.selenium.current_url)
        # Click buy button
        #self.selenium.find_element_by_xpath('/html/body/form/input[13]').click()
        #time.sleep(5)
        #self.assertEqual('%s%s' % (self.testdata['server_address'], '/weddingServices/'), self.selenium.current_url)


    def test_florist_successful_book(self):
        # Login
        self.helper.login()

        # Navigate to caterer list
        self.selenium.find_element_by_xpath('/html/body/div[1]/a[3]').click()
        # Navigate to caterer detail
        self.selenium.find_element_by_xpath('/html/body/div[2]/div/div/div[1]/h3/a').click()
        # Navigate to caterer booking
        self.selenium.find_element_by_xpath('/html/body/div[2]/div/div/a').click()
        # Select month from drop down
        self.selenium.find_element_by_xpath("//*[@id='id_booking_date_month']/option[text()='January']").click()
        # Select day from drop down
        self.selenium.find_element_by_xpath("//*[@id='id_booking_date_day']/option[text()='1']").click()
        # Select year from drop down
        self.selenium.find_element_by_xpath("//*[@id='id_booking_date_year']/option[text()='2018']").click()
        # Select time slot AN
        self.selenium.find_element_by_xpath("//*[@id='id_time_slots_1']").click()
        # Click book button
        self.selenium.find_element_by_xpath('/html/body/form/button').click()
        self.assertIn('http://127.0.0.1:8000/weddingServices/florists/2/bookdate', self.selenium.current_url)
        # Click buy button
        #self.selenium.find_element_by_xpath('/html/body/form/input[13]').click()
        #time.sleep(5)
        #self.assertEqual('%s%s' % (self.testdata['server_address'], '/weddingServices/'), self.selenium.current_url)

        
        
    def test_caterer_unsuccessful_book(self):
        # Login
        self.helper.login()

        # Navigate to caterer list
        self.selenium.find_element_by_xpath('/html/body/div[1]/a[2]').click()
        # Navigate to caterer detail
        self.selenium.find_element_by_xpath('/html/body/div[2]/div/div/div[3]/h3/a').click()
        # Navigate to caterer booking
        self.selenium.find_element_by_xpath('/html/body/div[2]/div/div/a').click()
        # Select month from drop down
        self.selenium.find_element_by_xpath("//*[@id='id_booking_date_month']/option[text()='December']").click()
        # Select day from drop down
        self.selenium.find_element_by_xpath("//*[@id='id_booking_date_day']/option[text()='25']").click()
        # Select year from drop down
        self.selenium.find_element_by_xpath("//*[@id='id_booking_date_year']/option[text()='2017']").click()
        # Select time slot AN
        self.selenium.find_element_by_xpath("//*[@id='id_time_slots_1']").click()
        # Click book button
        self.selenium.find_element_by_xpath('/html/body/form/button').click()
        error_message = self.selenium.find_element_by_xpath('/html/body/form/p[2]')
        self.assertEqual(error_message.text, 'Sorry Date is already booked. Please choose another.')        

    def test_florist_unsuccessful_book(self):
        # Login
        self.helper.login()

        # Navigate to caterer list
        self.selenium.find_element_by_xpath('/html/body/div[1]/a[3]').click()
        # Navigate to caterer detail
        self.selenium.find_element_by_xpath('/html/body/div[2]/div/div/div[1]/h3/a').click()
        # Navigate to caterer booking
        self.selenium.find_element_by_xpath('/html/body/div[2]/div/div/a').click()
        # Select month from drop down
        self.selenium.find_element_by_xpath("//*[@id='id_booking_date_month']/option[text()='December']").click()
        # Select day from drop down
        self.selenium.find_element_by_xpath("//*[@id='id_booking_date_day']/option[text()='25']").click()
        # Select year from drop down
        self.selenium.find_element_by_xpath("//*[@id='id_booking_date_year']/option[text()='2017']").click()
        # Select time slot AN
        self.selenium.find_element_by_xpath("//*[@id='id_time_slots_1']").click()
        # Click book button
        self.selenium.find_element_by_xpath('/html/body/form/button').click()
        error_message = self.selenium.find_element_by_xpath('/html/body/form/p[2]')
        self.assertEqual(error_message.text, 'Sorry Date is already booked. Please choose another.')

    def test_hall_unsuccessful_book(self):
        # Login
        self.helper.login()

        # Navigate to caterer list
        self.selenium.find_element_by_xpath('/html/body/div[1]/a[1]').click()
        # Navigate to caterer detail
        self.selenium.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/h3/a').click()
        # Navigate to caterer booking
        self.selenium.find_element_by_xpath('/html/body/div[2]/div/div/a').click()
        # Select month from drop down
        self.selenium.find_element_by_xpath("//*[@id='id_booking_date_month']/option[text()='December']").click()
        # Select day from drop down
        self.selenium.find_element_by_xpath("//*[@id='id_booking_date_day']/option[text()='25']").click()
        # Select year from drop down
        self.selenium.find_element_by_xpath("//*[@id='id_booking_date_year']/option[text()='2017']").click()
        # Select time slot AN
        self.selenium.find_element_by_xpath("//*[@id='id_time_slots_1']").click()
        # Click book button
        self.selenium.find_element_by_xpath('/html/body/form/button').click()
        error_message = self.selenium.find_element_by_xpath('/html/body/form/p[2]')
        self.assertEqual(error_message.text, 'Sorry Date is already booked. Please choose another.')

        

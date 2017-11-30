

class TestHelper:
    # Class to include all helper functions
    def login(self):
        try:
            self.selenium.get('%s%s' % (self.testdata['server_address'], '/login/'))
            username_input = self.selenium.find_element_by_name("username")
            username_input.send_keys(self.testdata['created_user']['username'])
            password_input = self.selenium.find_element_by_name("password")
            password_input.send_keys(self.testdata['created_user']['password'])
            self.selenium.find_element_by_xpath('//button').click()
        except StaleElementReferenceException:
            pass

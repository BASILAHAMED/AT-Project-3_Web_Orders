from selenium import webdriver
from selenium.webdriver.common.by import By
from Test_Data import login_data
import pytest


class TestLogin:
    url = "http://secure.smartbearsoftware.com/samples/TestComplete11/WebOrders/Login.aspx"
    
    # Launching driver for running the Python Tests
    @pytest.fixture
    def launch_driver(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(8)
        yield
        self.driver.close()
    
    def test_login1(self, launch_driver):
        self.driver.get(self.url)
        self.driver.find_element(by=By.XPATH, value=login_data.ElementLocators.xpath_username).send_keys(login_data.LoginData.username1) # verify with username1
        self.driver.find_element(by=By.XPATH, value=login_data.ElementLocators.xpath_password).send_keys(login_data.LoginData.password1)
        self.driver.find_element(by=By.XPATH, value=login_data.ElementLocators.xpath_login).click()
        warning = self.driver.find_element(by=By.XPATH, value=login_data.ElementLocators.xpath_invalid_login).text
        assert warning == 'Invalid Login or Password.'
        print("SUCCESS # INVALID LOGIN WITH USERNAME {username} and PASSWORD {password}".format(username=login_data.LoginData.username1, password=login_data.LoginData.password1))

    def test_login2(self, launch_driver):
        self.driver.get(self.url)
        self.driver.find_element(by=By.XPATH, value=login_data.ElementLocators.xpath_username).send_keys(login_data.LoginData.username2)
        self.driver.find_element(by=By.XPATH, value=login_data.ElementLocators.xpath_password).send_keys(login_data.LoginData.password2)
        self.driver.find_element(by=By.XPATH, value=login_data.ElementLocators.xpath_login).click()
        warning = self.driver.find_element(by=By.XPATH, value=login_data.ElementLocators.xpath_invalid_login).text
        assert warning == 'Invalid Login or Password.'
        print("SUCCESS # INVALID LOGIN WITH USERNAME {username} and PASSWORD {password}".format(username=login_data.LoginData.username3, password=login_data.LoginData.password2))
              
    def test_login3(self, launch_driver):
        self.driver.get(self.url)
        self.driver.find_element(by=By.XPATH, value=login_data.ElementLocators.xpath_username).send_keys(login_data.LoginData.username3)
        self.driver.find_element(by=By.XPATH, value=login_data.ElementLocators.xpath_password).send_keys(login_data.LoginData.password3)
        self.driver.find_element(by=By.XPATH, value=login_data.ElementLocators.xpath_login).click()
        warning = self.driver.find_element(by=By.XPATH, value=login_data.ElementLocators.xpath_invalid_login).text
        assert warning == 'Invalid Login or Password.'
        print("SUCCESS # INVALID LOGIN WITH USERNAME {username} and PASSWORD {password}".format(username=login_data.LoginData.username3, password=login_data.LoginData.password3))

    def test_login4(self, launch_driver):
        self.driver.get(self.url)
        self.driver.find_element(by=By.XPATH, value=login_data.ElementLocators.xpath_username).send_keys(login_data.LoginData.username4)
        self.driver.find_element(by=By.XPATH, value=login_data.ElementLocators.xpath_password).send_keys(login_data.LoginData.password4)
        self.driver.find_element(by=By.XPATH, value=login_data.ElementLocators.xpath_login).click()
        info = self.driver.find_element(by=By.XPATH, value=login_data.ElementLocators.xpath_login_info).text
        assert info == 'Welcome, Tester! | Logout'
        print("SUCCESS # LOGGED IN WITH USERNAME {username} and PASSWORD {password}".format(username=login_data.LoginData.username4, password=login_data.LoginData.password4))

    def test_logout(self, launch_driver):
        self.driver.get(self.url)
        self.driver.find_element(by=By.XPATH, value=login_data.ElementLocators.xpath_username).send_keys(login_data.LoginData.username4)
        self.driver.find_element(by=By.XPATH, value=login_data.ElementLocators.xpath_password).send_keys(login_data.LoginData.password4)
        self.driver.find_element(by=By.XPATH, value=login_data.ElementLocators.xpath_login).click()
        self.driver.implicitly_wait(4)
        self.driver.find_element(by=By.XPATH, value=login_data.ElementLocators.xpath_logout).click()
        username_box = self.driver.find_element(by=By.XPATH, value=login_data.ElementLocators.xpath_username_box).text
        assert username_box == 'Username:' 
        print("SUCCESS # LOGGED OUT")

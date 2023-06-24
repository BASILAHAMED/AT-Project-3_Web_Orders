class LoginData:
    # testing with all possible username password combinations
    # combo1
    username1 = 'Tester'
    password1 = 'password'
    # combo2
    username2 = 'username'
    password2 = 'test'
    # combo3
    username3 = 'username'
    password3 = 'password'
    # combo4
    username4 = 'Tester'
    password4 = 'test'

class ElementLocators:
    xpath_username = '//input[@id="ctl00_MainContent_username"]'
    xpath_password = '//input[@id="ctl00_MainContent_password"]'
    xpath_login = '//input[@id="ctl00_MainContent_login_button"]'
    xpath_invalid_login = '//span[@id="ctl00_MainContent_status"]'
    xpath_login_info = '//div[@class="login_info"]'
    xpath_username_box = '//label[@for="ctl00_MainContent_username"]'
    xpath_logout = '//a[@id="ctl00_logout"]'


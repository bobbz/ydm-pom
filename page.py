from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from element import BasePageElement
from locators import *

class BasePage(object):
    def __init__(self, driver):
        self.driver = driver

class MainPage(BasePage):

    def __init__(self):
        pass


class LoginPage(BasePage):

    def __init__(self, _driver):
        self.driver = _driver
        self.txt_username = self.driver.find_element(*LoginPageLocators.USERNAME_TEXTBOX)
        self.txt_password = self.driver.find_element(*LoginPageLocators.PASSWORD_TEXTBOX)
        self.btn_login = self.driver.find_element(*LoginPageLocators.LOGIN_BUTTON)
        self.chk_remember = self.driver.find_element(*LoginPageLocators.REMEMBERME_CHECKBOX)
        self.lnk_forgot = self.driver.find_element(*LoginPageLocators.FORGOTPWD_LINK)

    @property
    def title(self):
        return self.driver.title

    def signin(self, username, password):
        self.txt_username.clear()
        self.txt_username.clear()
        self.txt_username.send_keys(username)
        self.txt_password.send_keys(password)
        self.btn_login.click()
        return NavBar(self.driver)


class NavBar(BasePage):

    def __init__(self, _driver):
        self.driver = _driver
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "loginUserLiMenu"))
            )
        except EC.NoSuchElementException:
            self.driver.quit()
        finally:
            pass

        self.txt_caseid = self.driver.find_element(*NavBarLocators.CASEID_INPUT)
        self.btn_searchcase = self.driver.find_element(*NavBarLocators.SEARCHCASE_BUTTON)
        self.dp_menu = self.driver.find_element(*NavBarLocators.LOGINUSERLIMENU_DROPDOWN)
        self.txt_username = self.driver.find_element(*NavBarLocators.LOGINUSERNAME_SPAN).text

    @property
    def login_name(self):
        return self.txt_username

    def search_case(self, case_id):
        self.txt_caseid.clear()
        self.txt_caseid.send_keys(case_id)
        self.btn_searchcase.click()
        return CaseDetailPage(self.driver)

    def goto_userinfo(self):
        self.dp_menu.click()
        self.driver.find_element(*NavBarLocators.LGOINUSERINFO_LINK).click()
        return CaseDetailPage(self.driver)

    def logout(self):
        self.dp_menu.click()
        self.driver.find_element(*NavBarLocators.LOGOUT_LINK).click()
        return LoginPage(self.driver)


class SideBar(BasePage):
    pass


class CaseDetailPage(BasePage):
    pass

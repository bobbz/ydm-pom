from selenium.webdriver.common.by import By


class SearchResultsPageLocators(object):
    """一个搜索结果定位器类，所有搜索结果定位器应该来自这里"""
    pass


class LoginPageLocators(object):
    USERNAME_TEXTBOX = (By.ID, 'username')
    PASSWORD_TEXTBOX = (By.ID, 'password')
    FORGOTPWD_LINK = (By.LINK_TEXT,'Forgot password?')
    REMEMBERME_CHECKBOX = (By.ID, 'remember-me')
    REMEMBERME_LABEL = (By.TAG_NAME, 'label')
    LOGIN_BUTTON = (By.ID, 'button1')


class NavBarLocators(object):
    LOGINUSERNAME_SPAN = (By.ID, "loginUserName")

    CASEID_INPUT = (By.ID, "headCaseId")
    SEARCHCASE_BUTTON = (By.XPATH, "//i[@onclick='headShowCaseInfo();']")
    LOGINUSERLIMENU_DROPDOWN = (By.ID, "loginUserLiMenu")
    LGOINUSERINFO_LINK = (By.ID, "loginUserInfo")
    LOGOUT_LINK = (By.LINK_TEXT, "退出")
    
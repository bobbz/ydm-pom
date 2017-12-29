from selenium.webdriver.common.by import By

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


class SideBarLocators(object):
    SIDEBARNAV_DIV = (By.ID,"id=sidebar-nav")
    SIDEBAR_OVERVIEW_SPAN = (By.XPATH, "//ul[@id='dashboard-menu']/li/a/span")
    SIDEBAR_CASEIMPORT_SPAN = (By.XPATH, "//ul[@id='dashboard-menu']/li[2]/a/span")
    SIDEBAR_CASELIST_SPAN = (By.XPATH, "//ul[@id='dashboard-menu']/li[3]/a/span")
    SIDEBAR_ENGINE_SPAN = (By.XPATH, "//ul[@id='dashboard-menu']/li[4]/a/span")
    SIDEBAR_COMPANYINFO_SPAN = (By.XPATH, "//ul[@id='dashboard-menu']/li[5]/a/span")
    SIDEBAR_MSGMANAGE_SPAN = (By.XPATH, "//ul[@id='dashboard-menu']/li[6]/a/span")
    SIDEBAR_MSGMANAGE_LABEL_SPAN =(By.XPATH,"//ul[@id='dashboard-menu']/li[6]/ul/li/a/span")
    SIDEBAR_MSGMANAGE_KEYWORD_SPAN = (By.XPATH, "//ul[@id='dashboard-menu']/li[6]/ul/li[2]/a/span")
    SIDEBAR_ACCOUNTMANAGE_SPAN = (By.XPATH, "//ul[@id='dashboard-menu']/li[7]/a/span")
    SIDEBAR_REPORT_SPAN = (By.XPATH, "//ul[@id='dashboard-menu']/li[8]/a/span")
    SIDEBAR_TESTENGINE_SPAN = (By.XPATH, "//ul[@id='dashboard-menu']/li[9]/a/span")
    SIDEBAR_CALLCENTER_SPAN = (By.XPATH, "//ul[@id='dashboard-menu']/li[10]/a/span")


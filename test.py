import unittest
from selenium import webdriver
import page
from JsonDataManager import JsonData


class FlashCatLogin(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        jsData = JsonData(r"D:\ydm-pom\values.json")
        self.driver.get(jsData.get_value("url"))

    def test_login(self):
        login_page = page.LoginPage(self.driver)
        assert (login_page.title == "云电猫后台管理系统"), "登陆页面加载失败"
        login_page.signin("*****","******").logout()
        #assert self.driver.current_url.endswith("main"), "登陆失败"

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()

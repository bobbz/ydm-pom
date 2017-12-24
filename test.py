import unittest
from selenium import webdriver
import page


class FlashCatLogin(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get(r"url")

    def test_login(self):
        login_page = page.LoginPage(self.driver)
        assert (login_page.title == "云电猫后台管理系统"), "登陆页面加载失败"
        login_page.signin("*****","******").logout()
        #assert self.driver.current_url.endswith("main"), "登陆失败"

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()

# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
import time, unittest

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

class testAddGroup(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver(capabilities={"marionette": False})
        self.wd.implicitly_wait(60)
    
    def test_testAddGroup(self):
        success = True
        wd = self.wd
        wd.get("http://macbook-pro-123.local/addressbook/index.php")
        ActionChains(wd).move_to_element(wd.find_element_by_name("user")).perform()
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys("admin")
        ActionChains(wd).move_to_element(wd.find_element_by_id("content")).perform()
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").send_keys("\\9")
        ActionChains(wd).move_to_element(wd.find_element_by_css_selector("html")).perform()
        ActionChains(wd).move_to_element(wd.find_element_by_id("content")).perform()
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys("secret")
        ActionChains(wd).move_to_element(wd.find_element_by_link_text("Forgot password")).perform()
        ActionChains(wd).move_to_element(wd.find_element_by_id("content")).perform()
        ActionChains(wd).move_to_element(wd.find_element_by_link_text("Create account")).perform()
        ActionChains(wd).move_to_element(wd.find_element_by_id("LoginForm")).perform()
        ActionChains(wd).move_to_element(wd.find_element_by_xpath("//form[@id='LoginForm']/input[3]")).perform()
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").send_keys("\\undefined")
        wd.find_element_by_xpath("//form[@id='LoginForm']/input[3]").click()
        ActionChains(wd).move_to_element(wd.find_element_by_id("content")).perform()
        ActionChains(wd).move_to_element(wd.find_element_by_css_selector("hr")).perform()
        ActionChains(wd).move_to_element(wd.find_element_by_id("content")).perform()
        ActionChains(wd).move_to_element(wd.find_element_by_name("searchform")).perform()
        ActionChains(wd).move_to_element(wd.find_element_by_id("search-az")).perform()
        ActionChains(wd).move_to_element(wd.find_element_by_id("content")).perform()
        ActionChains(wd).move_to_element(wd.find_element_by_id("nav")).perform()
        ActionChains(wd).move_to_element(wd.find_element_by_link_text("groups")).perform()
        wd.find_element_by_link_text("groups").click()
        ActionChains(wd).move_to_element(wd.find_element_by_link_text("groups")).perform()
        ActionChains(wd).move_to_element(wd.find_element_by_id("nav")).perform()
        ActionChains(wd).move_to_element(wd.find_element_by_xpath("//div[@id='content']//h1[.='Groups']")).perform()
        ActionChains(wd).move_to_element(wd.find_element_by_id("content")).perform()
        ActionChains(wd).move_to_element(wd.find_element_by_name("new")).perform()
        wd.find_element_by_name("new").click()
        ActionChains(wd).move_to_element(wd.find_element_by_css_selector("label")).perform()
        ActionChains(wd).move_to_element(wd.find_element_by_xpath("//div[@id='content']/form")).perform()
        ActionChains(wd).move_to_element(wd.find_element_by_name("group_name")).perform()
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys("testGroup")
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys("test")
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys("teste")
        ActionChains(wd).move_to_element(wd.find_element_by_xpath("//div[@id='content']/form")).perform()
        ActionChains(wd).move_to_element(wd.find_element_by_name("group_footer")).perform()
        ActionChains(wd).move_to_element(wd.find_element_by_xpath("//div[@id='content']/form")).perform()
        ActionChains(wd).move_to_element(wd.find_element_by_name("submit")).perform()
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").send_keys("\\undefined")
        wd.find_element_by_name("submit").click()
        ActionChains(wd).move_to_element(wd.find_element_by_css_selector("html")).perform()
        ActionChains(wd).move_to_element(wd.find_element_by_id("footer")).perform()
        ActionChains(wd).move_to_element(wd.find_element_by_link_text("v8.2.5")).perform()
        ActionChains(wd).move_to_element(wd.find_element_by_css_selector("div.msgbox")).perform()
        ActionChains(wd).move_to_element(wd.find_element_by_link_text("group page")).perform()
        wd.find_element_by_link_text("group page").click()
        ActionChains(wd).move_to_element(wd.find_element_by_xpath("//div[@id='content']/form")).perform()
        ActionChains(wd).move_to_element(wd.find_element_by_link_text("print phones")).perform()
        ActionChains(wd).move_to_element(wd.find_element_by_xpath("//div[@id='nav']//li[normalize-space(.)='print phones']")).perform()
        ActionChains(wd).move_to_element(wd.find_element_by_id("header")).perform()
        ActionChains(wd).move_to_element(wd.find_element_by_xpath("//div[@id='content']/form")).perform()
        ActionChains(wd).move_to_element(wd.find_element_by_id("content")).perform()
        ActionChains(wd).move_to_element(wd.find_element_by_id("header")).perform()
        ActionChains(wd).move_to_element(wd.find_element_by_id("top")).perform()
        ActionChains(wd).move_to_element(wd.find_element_by_css_selector("html")).perform()
        ActionChains(wd).move_to_element(wd.find_element_by_link_text("Logout")).perform()
        wd.find_element_by_link_text("Logout").click()
        ActionChains(wd).move_to_element(wd.find_element_by_id("top")).perform()
        self.assertTrue(success)
    
    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()

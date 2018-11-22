import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class Blog_ATS(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_blog(self):
        #Logging into the blog
        user = 'instructor'
        password = 'instructor1a'
        driver = self.driver
        driver.maximize_window()
        driver.get('http://127.0.0.1:8000/admin')
        elem = driver.find_element_by_id('id_username')
        elem.send_keys(user)
        elem = driver.find_element_by_id('id_password')
        elem.send_keys(password)
        time.sleep(3)
        elem.send_keys(Keys.RETURN)
        assert('Logged In')
        time.sleep(3)

        #Posting to Blog
        driver.get('http://127.0.0.1:8000/')
        time.sleep(2)
        driver.find_element_by_xpath('/html/body/div[1]/a/span').click()
        time.sleep(3)
        elem = driver.find_element_by_id('id_title')
        elem.send_keys('Test Title')
        elem = driver.find_element_by_id('id_text')
        elem.send_keys('Test Body of the Blog, which is supposed to have random texts')
        time.sleep(3)
        driver.find_element_by_xpath('/html/body/div[2]/div/div/form/button').click()
        time.sleep(3)
        assert('Posted Blog Entry')
        driver.get('http://127.0.0.1:8000/')
        time.sleep(3)


    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
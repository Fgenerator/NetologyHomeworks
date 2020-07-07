from selenium import webdriver
import time
import unittest


class TestUI(unittest.TestCase):
    def setUp(self):
        path_dr = 'chromedriver.exe'
        self.driver = webdriver.Chrome(executable_path=path_dr)

        self.driver.implicitly_wait(30)
        self.driver.get('https://passport.yandex.ru/auth')

        time.sleep(1)

    def test_login_yandex(self):

        xpath_passp_field_login = '//*[@id="passp-field-login"]'
        xpath_enter = '//*[@id="root"]/div/div/div[2]/div/div/div[3]/div[2]/div/div/div[1]/form/div[3]/button'

        passp_field_login = self.driver.find_element_by_xpath(xpath_passp_field_login)

        enter_button = self.driver.find_element_by_xpath(xpath_enter)

        passp_field_login.send_keys('')  # yandex login
        time.sleep(1)
        enter_button.click()

        time.sleep(1)
        xpath_passp_field_passwd = '//*[@id="passp-field-passwd"]'
        passp_field_passwd = self.driver.find_element_by_xpath(xpath_passp_field_passwd)
        passp_field_passwd.send_keys('')  # yandex password

        time.sleep(1)
        xpath_enter_passw_button = '//*[@id="root"]/div/div/div[2]/div/div/div[3]/div[2]/div/div/form/div[2]/button'
        enter_passw_button = self.driver.find_element_by_xpath(xpath_enter_passw_button)
        enter_passw_button.click()

        time.sleep(1)

        xpath_email = '//*[@id="root"]/div/div[2]/div[1]/div/div/a[1]/span[1]'
        email = self.driver.find_element_by_xpath(xpath_email)

        self.assertIsNotNone(email)





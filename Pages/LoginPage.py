from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    def getPage(self):
        self.driver.get("https://9gag.com/login")

    def closePopUp(self):
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "popup_content--2JBXA")))
            self.driver.find_element_by_xpath("/html/body/div[7]/div[1]/div[2]/div/div[3]/button[2]").click()
        except NoSuchElementException:
            print('Element not found')

    def putUsername(self, username):
        self.driver.find_element_by_id("login-email-name").clear()
        self.driver.find_element_by_id("login-email-name").send_keys(username)

    def putPassword(self, password):
        self.driver.find_element_by_id("login-email-password").clear()
        self.driver.find_element_by_id("login-email-password").send_keys(password)

    def clickLogin(self):
        popUp = self.driver.find_element_by_id("signup")
        if popUp.is_displayed():
            self.driver.find_element_by_xpath("//*[@id=\"login-email\"]/div[3]/input").click()

    def successfulPage(self):
        if self.driver.find_element_by_id("jsid-upload-btn").is_displayed():
            return True
        else:
            return False

    def unsuccessfulPage(self):
        if self.driver.find_element_by_xpath("//*[@id=\"login-email\"]/div[2]/p").is_displayed():
            return True
        else:
            return False

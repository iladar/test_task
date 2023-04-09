from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests


class BasePage:

    def __init__(self, driver, base_url):
        self.driver = driver
        self.base_url = base_url

    def find_element(self, locator, time=10):
        wait = WebDriverWait(self.driver, time, 0.3)
        element = wait.until(EC.presence_of_element_located(locator), message='Element wasnt found')
        return element

    def find_elements(self, locator, time=10):
        wait = WebDriverWait(self.driver, time, 0.3)
        element = wait.until(EC.presence_of_all_elements_located(locator), message='Element wasnt found')
        return element

    def get_element_text(self, locator, time=10):
        element = self.find_element(locator,time)
        return element.text

    def is_present(self, locator):
        return len(self.find_elements(locator)) > 0

    def go_to_site(self):
        return self.driver.get(self.base_url)

    def go_to_link(self, link):
        return self.driver.get(link)

    def go_to_main_window(self):
        self.driver.switch_to.window(self.driver.window_handles[0])

    def go_to_chosen_window(self, num):
        self.driver.switch_to.window(self.driver.window_handles[num])

    def get_current_url(self):
        return self.driver.current_url

    def get_link_url(self, link):
        url = link.get_attribute('href')
        return requests.get(url).url

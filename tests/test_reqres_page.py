from BaseApp import BasePage
from selenium.webdriver.common.by import By
import requests


def test_reqres_page(setup):
    page = BasePage(setup, 'https://reqres.in/')
    page.go_to_site()
    url = page.get_current_url()
    assert url == "https://reqres.in/"
    endpoints = page.find_elements((By.CSS_SELECTOR, '.endpoints li'))
    for endpoint in endpoints:
        endpoint.click()
        method = endpoint.get_attribute('data-http')
        if method != 'get':
            continue
        request_endpoint = page.get_element_text((By.CSS_SELECTOR, '.request .url'))
        request_url = 'https://reqres.in' + request_endpoint
        r = requests.get(request_url)
        responses_text = r.text
        text = page.get_element_text((By.CSS_SELECTOR, '.response pre'))
        text = text.replace(' ', '')
        text = text.replace('\n', '')
        responses_text = responses_text.replace(' ', '')
        responses_text = responses_text.replace('\n', '')
        assert text == responses_text



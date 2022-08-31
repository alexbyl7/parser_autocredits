import requests
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from bs4 import BeautifulSoup
import time


def get_html_requests(url):
    r = requests.get(url)
    return r.text


def get_html_webdriver(url):
    options = Options()
    options.headless = True
    driver = webdriver.Firefox(options=options)
    driver.get(url)
    time.sleep(1)
    html = driver.page_source
    driver.close()
    return html


def get_soup(url):
    h = get_html_webdriver(url)
    return BeautifulSoup(h, 'html.parser')

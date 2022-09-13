import requests
from selenium import webdriver
# from selenium.webdriver.firefox.options import Options
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time


def get_html_requests(url):
    r = requests.get(url)
    return r.text


def get_html_webdriver(url):
    # firefox_profile = webdriver.FirefoxProfile()
    # firefox_profile.set_preference('permissions.default.image', 2)
    # firefox_profile.set_preference('dom.ipc.plugins.enabled.libflashplayer.so', 'false')

    options = Options()
    # options.headless = True
    options.add_argument('--headless')

    print("Страница ", url)
    print("Загрузка драйвера... ", end='', flush=True)
    # driver = webdriver.Firefox(options=options, firefox_profile=firefox_profile)
    driver = webdriver.Chrome(chrome_options=options)
    # driver = webdriver.Chrome()

    print("Драйвер загружен")

    print("Загрузка страницы... ", end='', flush=True)
    driver.get(url)
    time.sleep(1)
    html = driver.page_source
    driver.close()
    print("Страница загружена")
    time.sleep(1)

    return html


def get_soup(url):
    h = get_html_webdriver(url)
    return BeautifulSoup(h, 'html.parser')

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

import seleniumbase as sb
from selenium_stealth import stealth
from bs4 import BeautifulSoup
from bs4.element import Tag


def open_url(url):
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    options.add_argument("start-maximized")
    options.add_argument("--headless")
    
    driver = sb.Driver(browser='chrome', headless=True, uc=True)
    wait = webdriver.Chrome.implicitly_wait(driver, 500.00)

    stealth(driver,
            languages=['ru-Ru', 'ru'],
            vendor='Google Inc.',
            platform='Win64',
            webgl_vendor='Intel Inc.',
            renderer='Intel Iris OpenGL Engine',
            fix_hairline=True,
            wait=wait
            )
    driver.get(url)
    try:
        # ждем пока не появится на странице тэг с id ozonTagManagerApp
        element = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.ID, "ozonTagManagerApp"))
        )
    finally:
        # возвращаем текст страницы
        return driver.page_source


def parse_page(page_source, products_count: int):
    soup = BeautifulSoup(page_source, 'html.parser')
    # soup = BeautifulSoup(open('page.html'))
    items_body = soup.find('div', id = 'paginatorContent')
    items = items_body.div.div
    data = []
    idx = 0
    for sibling in items:
        if idx >= products_count:
            break
        if isinstance(sibling, Tag) and sibling.text:
            data.append({
                'name': sibling.div.a.next_sibling.next_sibling.a.div.span.text.split('/')[0],
                'price': int(sibling.a.next_sibling.next_sibling.div.div.span.text.encode('ascii', 'ignore')),
                'description': sibling.div.a.next_sibling.next_sibling.a.div.span.text,
                'image_url': sibling.div.select_one('div > img')['src'],
                'discount': sibling.a.next_sibling.next_sibling.div.div.span.next_sibling.next_sibling.text
            })
            idx += 1
    return data

def get_data_from_website(products_count):
    url = 'https://www.ozon.ru/seller/1/products/'
    page_source = open_url(url)
    return parse_page(page_source, products_count)

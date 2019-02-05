import requests
from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import pandas as pd


zipcode = "92840"
url = "https://www.airbnb.com/s/all?refinement_paths%5B%5D=%2Ffor_you&query=92840&adults=0&children=0&infants=0&guests=0"


# def create_url(zipcode):
#     url = f"https://www.airbnb.com/s/all?refinement_paths%5B%5D=%2Ffor_you&query={zipcode}&adults=0&children=0&infants=0&guests=0"
#     return get_page(url)


def get_page(driver, url):
    driver.get(url)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    counter = 1
    div_class = soup.div['_aov0j6']
    for link in div_class.find_all('a'):
        link_url = link.get('href')
        if '/rooms/' in link_url:
            print(f"{counter}) {link_url}")
            counter += 1
    print(f"{counter - 1} total rooms.")
    driver.close()


def main():
    get_page(webdriver.Firefox(), url)
    # soup = get_page(webdriver.Firefox() ,url)
    # print(soup.prettify())


if __name__ == "__main__":
    main()

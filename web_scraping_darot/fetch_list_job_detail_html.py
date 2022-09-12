
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import pandas as pd


def fetch_html_to_file(file_name, url):
    PATH = "/Users/darotchen/Desktop/Web Scraping/chromedriver"
    service = Service(PATH)
    driver = webdriver.Chrome(service=service)
    print(url)
    driver.get(url)
    with open(file_name, 'w') as f:
        f.write(driver.page_source)
    driver.quit()


def read_from_file(file_name):
    with open(file_name, 'r') as f:
        content = f.read()
        return content


if __name__ == '__main__':
    job_list_links = read_from_file('job_list/job_list.txt').split('\n')
    for index, job_link in enumerate(job_list_links):
        fetch_html_to_file(f'job_details/{index}_job_detail.html', job_link)

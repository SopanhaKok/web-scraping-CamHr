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


def read_html_file(file_name):
    with open(file_name, 'r') as f:
        html = f.read()
        return html


def find_job_detail_link(job_info):
    job_detail = 'https://camhr.com/a' + job_info.a['href'][1:]
    return job_detail


def write_job_list_to_file(job_list):
    with open('job_list/job_list.txt', 'w') as f:
        for index, job in enumerate(job_list):
            f.write(f'{job} \n')


def fetch_job_list():
    soup = BeautifulSoup(read_html_file('job_list.html'), 'html.parser')
    job_items = soup.find_all('div', class_="job-item")
    list_job_links_detail = []
    for job_item in job_items:
        list_job_links_detail.append(find_job_detail_link(
            job_item.find('div', class_="jobs-info")))
    # print(list_job_links_detail)
    return list_job_links_detail


if __name__ == '__main__':
    job_list = fetch_job_list()
    write_job_list_to_file(job_list)

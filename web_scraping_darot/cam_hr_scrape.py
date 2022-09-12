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


def find_job():
    with open('job_list.html', 'r') as fp:
        soup = BeautifulSoup(fp, 'html.parser')

    job_items = soup.find_all('div', class_="job-item")
    job_titles = []
    job_details = []
    job_levels = []
    company_names = []
    terms = []
    locations = []
    salaries = []
    for job_item in job_items:
        job_title, job_detail, job_level = find_job_info(
            job_item.find('div', class_="jobs-info"))
        job_titles.append(job_title)
        job_details.append(job_detail)
        job_levels.append(job_level)

        term, location, salary = find_other_info(
            job_item.find('span', class_="other-info"))
        terms.append(term)
        locations.append(location)
        salaries.append(salary)

        company_name = find_company_info(
            job_item.find('div', class_="company-info"))
        company_names.append(company_name)

    data = {
        'Job Titles': job_titles,
        'Job Detail link': job_details,
        'Job Level': job_levels,
        'Company': company_names,
        'Term': terms,
        'Location': locations,
        'Salaries': salaries,
    }

    df = pd.DataFrame(data)
    df.to_csv('job_list.csv', sep=',', encoding='utf-8')
    print(df.head())


def find_company_info(company_info):
    company_name = company_info.a.text
    company_detail = company_info.a['href']
    return company_name


def find_other_info(other_info):
    term, location = other_info.text.split('|')
    salary = other_info.find('span', class_="job-salary").text
    return [term, location, salary]


def find_job_info(job_info):
    job_title = job_info.a.text
    job_detail = 'https://camhr.com/a' + job_info.a['href'][1:]
    job_level = job_title[job_title.find('(') + 1: job_title.find(')')]
    return [job_title, job_detail, job_level]


if __name__ == '__main__':
    # find_job()
    # fetch_html_to_file(file_name='job_list.html',
    #                    url="https://www.camhr.com/a/job?page=1&param=%7B%22page%22%3A1,%22size%22%3A50%7D")
    fetch_html_to_file(file_name='job_details/job_detail_1.html',
                       url="https://camhr.com/a/job/10517052?title=IT training specialists and facilitators")

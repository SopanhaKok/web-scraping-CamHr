from opcode import opname
from queue import Empty
from bs4 import BeautifulSoup
import pandas as pd


def find_detail(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    job_title = soup.find('div', class_="job-name")
    job_date = job_title.find('div', class_="send-date")
    publish_date = job_date.find_all('span')[0].text
    close_date = job_date.find_all('span')[1].text

    company_profile = soup.find('div', class_="company-info").text
    contact_info = soup.find('div', class_="recruiter-info").text

    job_description, job_requirement = soup.find_all(
        'div', class_="job-descript")

    table = soup.find('table', class_="mailTable")
    table_detail = table.find_all('td')

    data = {
        'Job Title': [job_title.span.text],
        "Position": [job_title.span.text],
        "Level": [table_detail[0].text.strip('\n').replace(" ", "")],
        "Term": [table_detail[1].text.strip('\n').replace(" ", "")],
        "Year of Exp": [table_detail[2].text.strip('\n').replace(" ", "")],
        "Function": [table_detail[3].text.strip('\n').replace(" ", "")],
        "Hiring": [table_detail[4].text.strip('\n').replace(" ", "")],
        "Industry": [table_detail[5].text.strip('\n').replace(" ", "")],
        "Salary": [table_detail[6].text.strip('\n').replace(" ", "")],
        "Qualification": [table_detail[7].text.strip('\n').replace(" ", "")],
        "Sex": [table_detail[8].text.strip('\n').replace(" ", "")],
        "Age": [table_detail[10].text.strip('\n').replace(" ", "")],
        "Language": [table_detail[9].text.strip('\n').replace(" ", "")],
        "Location": [table_detail[11].text.strip('\n').replace(" ", "")],
        "Job Description": [job_description.find('div', class_="descript-list").text],
        "Job Requirement": [job_requirement.find('div', class_="descript-list").text],
        "Company Profile": [company_profile],
        "Contact Info": [contact_info],
        "Publish Date": [publish_date],
        "Close Date": [close_date],
    }

    df = pd.DataFrame(data)
    return df
    # print(df.shape)


if __name__ == '__main__':
    df = pd.DataFrame()
    for i in range(50):
        with open(f'job_details/{i}_job_detail.html', 'r') as f:
            data = find_detail(f)
            print(f"Index: {4}")
            print(data)
            if(df.empty):
                df = pd.DataFrame(data)
            else:
                df.append(data, ignore_index=True)
    # df.to_csv('job_list.csv', sep=',', encoding='utf-8')
    # print(df.shape())

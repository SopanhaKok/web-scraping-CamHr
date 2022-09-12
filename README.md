# web-scraping-CamHr

## Introduction
Job searching analysis is the process of scraping data from popular websites in Cambodia such as Bongthom, CamHr, Pel Prek or National Employment Agency websites etc. It involves collecting and recording job-related data such as knowledge and skills required to perform a job, duties and responsibilities involved, education qualifications and experience required and physical and emotional characteristics required to perform a job in a desired manner. 
We set up job data scraping processes to automatically extract newly posted jobs from the popular website and have more data to analyze. There are a number of techniques such as using Chrome extension , Python using libraries etc. So we will use the Web Scraper Chrome extension/ Python to scrape the data. 

## Project Objective
1. To have an overview what is the job needs (June & July Vs August & September)
2. Identifying reskilling and up-skilling opportunities. 
3. To understand which job is required for ICT.
4. To see the trend of job demand or the comparison between June & July and next two months

## Project Set up
### Programming 
In this project we use python programming `version: 3.9.7` to scraping data from the website [CamHR]("camhr.com/"). 

### Library
In this project we use [Selenium]("https://selenium-python.readthedocs.io/") and [BeautifulSoup]("https://beautiful-soup-4.readthedocs.io/en/latest/#quick-start") for scraping the data.

To install Selenium: 
```shell
pip install selenium
```

To install BeautifulSoup
```shell
pip install beautifulsoup4
```

### Tools
#### **Broswer**
For the browser we use Chrome and Chrome driver to help us for open the website and inspecting for scraping the data. 
> To install Chrome driver click [here]("https://chromedriver.chromium.org/downloads").

#### **Power BI**
This is the desktop application for Data Cleaning and Data virtualization.

> To install Power BI click [here]("https://www.microsoft.com/en-us/download/details.aspx?id=58494").

## Data

Here is the data set that we have scrape with arround 3000 rows.
Click here to get the [data]("https://docs.google.com/spreadsheets/d/1ZMNntYZ2ZKOes8lZ_q6Zn2Nou1D5a1SQKyd2fi9yJx4/edit#gid=936442396").
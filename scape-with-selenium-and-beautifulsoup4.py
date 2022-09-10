from  selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import pandas as pd
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By




PATH = "C:\Program Files (x86)\chromedriver.exe"
service = Service(PATH)
driver = webdriver.Chrome(service=service)
driver.set_page_load_timeout(100)
baseUrl = "https://www.camhr.com"
wait = WebDriverWait(driver,20)

def getUrlPerPage():
    urlList = []
    soup = BeautifulSoup(driver.page_source,"html.parser")
    jobs_list = soup.find('div',class_='jobs-list')
    job_items = jobs_list.find_all('div',class_="job-item")
    for job in job_items:
        anchorElement = job.find('a',class_="job-title")
        url = f'{baseUrl}/a{anchorElement["href"][1:]}'
        urlList.append(url)
    return urlList

def hasNextPage(currentPage):
    soup = BeautifulSoup(driver.page_source,"html.parser")
    paginationElement = soup.find('ul',class_="el-pager")
    liElement = paginationElement.find_all('li',class_="number")
    lastPage = liElement[-1].text
    if str(currentPage) == lastPage:
        return False
    return True
    


if __name__ == "__main__":
    urlList = []
    informations = []
    page = 1



    # Step 1 Get detail url from all the pages 
    while True:
        url = f'https://www.camhr.com/a/job?page={page}&param={{"page":{page},"size":50}}'
        driver.get(url)
        waitForJobItem = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME,'job-item')))
        urls = getUrlPerPage()
        urlList.extend(urls)
        if hasNextPage(page):
            page += 1
        else:
            break
    print(len(urlList))

    # Step 2 Get detail information of every posts from URL Lists
    for url in urlList:
        driver.get(url)
        mainInfo =  wait.until(EC.presence_of_element_located((By.CLASS_NAME,'job-maininfo')))
        soup = BeautifulSoup(driver.page_source,"html.parser")


        jobTitle = soup.find("span",class_='job-name-span').text

        table = soup.find("table",class_="mailTable")
        tableData = table.find_all("td")

        level = tableData[0].text
        term = tableData[1].text
        yearOfExp = tableData[2].text 
        function = tableData[3].text 
        hiring = tableData[4].text 
        industry = tableData[5].text 
        salary =  tableData[6].text 
        qualification=  tableData[7].text 
        sex =  tableData[8].text 
        language =  tableData[9].text 
        age =  tableData[10].text 
        location = tableData[11].text
        print(level,term,yearOfExp,function,hiring,industry,salary,qualification,sex,language,age)
        print(url,end="\n")
        try:
            jobDescription = soup.find_all('div',class_='job-descript')
            if len(jobDescription) == 2:
                description = jobDescription[0].find('div',class_="descript-list").text
                jobRequirement = jobDescription[1].find('div',class_="descript-list").text
            else:
                title = jobDescription[0].find('div',class_="descript-title").text
                if title == 'Job Requirements':
                    jobRequirement = jobDescription[0].find('div',class_="descript-list").text
                    description = ""
                else:
                    description = jobDescription[0].find('div',class_="descript-list").text
                    jobRequirement = ""
        except: 
            description = ""
            jobRequirement = ""
        
        

        jobDetail =  soup.find_all('div',class_='jobdetail-item')
        try:
            companyProfile = jobDetail[0].find('div',class_="company-info").text
        except:
            companyProfile = ""
        

        if companyProfile:
            companyContact = jobDetail[1].find('div',class_="recruiter-info")
        else:
            companyContact = jobDetail[0].find('div',class_="recruiter-info")
        recruiterName = companyContact.find('span',class_="recruiter-name").text
        recruiterJob = companyContact.find('span',class_="recruiter-job").text

        recruiterInformation = companyContact.find("div",class_="recruiter-baseinfo")
        recruiterInformation = recruiterInformation.find_all("a",class_="d-inline-block")
        try:
            recruiterNumber = recruiterInformation[0].text
        except:
            recruiterNumber = ""
        try:
            recruiterEmail = recruiterInformation[1].text
        except:
            recruiterEmail = ""
        try:
            recruiterLocation = recruiterInformation[2].text
        except:
            recruiterLocation = ""

        print(recruiterEmail,recruiterNumber,recruiterLocation,recruiterName,recruiterJob)
        sendDate = soup.find("div",class_="send-date")
        publishedDate = sendDate.find("span").text
        closeDate = sendDate.find("span",class_="close-date").text
        contact = f'Contact Information {recruiterName} {recruiterJob} {recruiterNumber} {recruiterEmail} {recruiterLocation} {recruiterNumber}'
        information = {"jobUrl": url,"job title":jobTitle,"position": jobTitle,"Level":level,"Year of Exp":yearOfExp,"Hiring":hiring,"Salary":salary,"Sex":sex,"Age":age,"Term":term,"Function/Category":function
        ,"Industry":industry,"Qualification":qualification,"Language":language,"Location":location,"Job Description":description,"Job Requirement":jobRequirement,"Company Profile":companyProfile,"Publish Date":publishedDate,"Closing Date":closeDate,
        "Contact Info": contact}
        informations.append(information)

    for info in informations:
        print(info)

    df = pd.DataFrame(informations)
    df.to_csv("camHr.csv")
    driver.quit()
    



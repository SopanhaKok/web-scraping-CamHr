from source.camHR.extractor import Extractor
from datetime import datetime
import pytz
import csv

from colorama import Fore, Style
import asyncio

camHRExtractor = Extractor()
async def main():
    keyword = input(
        f"{Fore.CYAN}Enter the keyword you want to search: {Style.RESET_ALL}"
    )
    
    now = datetime.now(pytz.timezone('Asia/Bangkok')) 

    page = 1
    limit = 50
    totalPage = 0
    items = []

    while True:
        url = f'https://api.camhr.com/v1.0.0/jobs?page={page}&size={limit}&locationId=0&jobTitleOrCompany={keyword}'

        res = await camHRExtractor.fetch_json_async(url)
        data = res["data"]
        totalPage = data["totalPage"]
        page += 1 

        jobs = data["result"]

        for job in jobs:
            exp_date = datetime.fromisoformat(job["expdate"])

            if exp_date < now: 
                continue  # Skip expired jobs but continue processing other jobs
                
            publish_date = datetime.fromisoformat(job.get('pubdate', ''))
            job_data = {
                'title': job.get('title', ''),
                'term': job.get('termId', {}).get('label',''),
                'hiring': job.get('hirelings','~'),
                'work_experience': job.get('workyears', ''),
                'age': f'From {job.get('ageFrom', '~')} To {job.get('ageTo','~')}',
                "sex": job.get('sex',{}).get('label',''),
                'location': job.get('location',''),
                'qualification': job.get('qualificationId', {}).get('label', ''),
                'requirement': job.get('requirement', ''),
                'description': job.get('description', ''),
                'publish_date': publish_date.strftime("%B %d, %Y at %I:%M %p"),
                'expiration_date': exp_date.strftime("%B %d, %Y at %I:%M %p"),
                'address': job.get('address', ''),
                'is_urgent': job.get('is_urgent', False),
                'contact_name': job.get('contact', {}).get('name', ''),
                'contact_phone': job.get('contact', {}).get('telephone', ''),
                'contact_email': job.get('contact', {}).get('email', ''),
                'salary': job.get('salaryId', {}).get('label', ''),
               
                'major': job.get('major', '')
            }
            
            items.append(job_data)
            
            print(f"{Fore.GREEN}Found job: {job_data['title']}{Style.RESET_ALL}")
            
        if page > totalPage: 
            break

    csv_filename = f"{keyword}_{now.strftime('%d%m%Y')}.csv"
    
    with open(csv_filename, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = list(items[0].keys()) if items else []
        
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        writer.writeheader()
        
        for job in items:
            writer.writerow(job)
    
    print(f"{Fore.CYAN}Successfully saved {len(items)} jobs to {csv_filename}{Style.RESET_ALL}")



if __name__ == "__main__":
    asyncio.run(main())

   

    
    



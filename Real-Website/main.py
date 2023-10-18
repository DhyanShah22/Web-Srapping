from bs4 import BeautifulSoup
import requests
import time


print('Add skills you are not familiar with')
unfamiliar_skill = input('>')
print(f'Filtering out {unfamiliar_skill}')

def find_job():
    html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text
    #print(html_text)
    soup = BeautifulSoup(html_text, 'lxml')
    jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')
    #print(job)
    for index, job in enumerate(jobs):

        publish = job.find('span', class_='sim-posted').span.text
        #print(publish)

        if 'few' in publish:
            company_name = job.find('h3', class_='joblist-comp-name').text.replace(' ','')  # repalce will replace white lines
            #print(company_name)

            skills_req = job.find('span', class_= 'srp-skills').text.replace(' ','')
            #print(skills_req)

            more_info = job.header.h2.a['href']

            #print(f''' 
            #Company Name: {company_name}
            #Required Skills: {skills_req}
            #''')

            if unfamiliar_skill not in skills_req:
                with open(f'Posts/{index}.txt', 'w') as f:
                    f.write(f"Company Nam: {company_name.strip()} \n")
                    f.write(f"Required Skills: {skills_req.strip()} \n")
                    f.write(f"More Info: {more_info} \n")

                print(f'File saved: {index}')
                    
                    #print('')

if __name__ == '__main__':
    while True:
        find_job()
        time_wait = 10
        print(f'Wainting {time_wait} minutes...')
        time.sleep(time_wait*60)
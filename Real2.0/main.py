from bs4 import BeautifulSoup
import requests
import time

html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text
#print(html_text)

soup = BeautifulSoup(html_text, 'lxml')
#jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')
#print(jobs)

# Here change find_all to find and jobs to job
jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')
#print(job)

#company_name = job.find('h3', class_='joblist-comp-name')
#print(company_name)
 
# after this we add text.replace(' ','' )

#company_name = job.find('h3', class_='joblist-comp-name').text.replace(' ','')
#print(company_name)

# Let's add skills now
#skills = job.find('span', class_='srp-skills').text.replace(' ','')
#print(skills)


#published_data = job.find('span', class_='sim-posted').span.text
#print(published_data)

#Now after this back to find_all in job and job to jobs and for loop

#print(f''' 
#Company Name: {company_name}
#Required Skills: {skills}
#''')

#### here we go

#for job in jobs:
#    company_name = job.find('h3', class_='joblist-comp-name').text.replace(' ','')
#    skills = job.find('span', class_='srp-skills').text.replace(' ','')
#    published_data = job.find('span', class_='sim-posted').span.text
    #print(published_data)

#   print(f''' 
#   Company Name: {company_name}
#   Required Skills: {skills}
#   ''')
#
#   print('')

# Now, once this is done we range it out in days term
for job in jobs:

    published_data = job.find('span', class_='sim-posted').span.text
    if 'few' in published_data:
        company_name = job.find('h3', class_='joblist-comp-name').text.replace(' ','')
        skills = job.find('span', class_='srp-skills').text.replace(' ','')
        

        # After prettify add more info
        more_info = job.header.h2.a['href']
        #print(published_data)

        #print(f''' 
        #Company Name: {company_name}
        #Required Skills: {skills}
        #''')

        # Now time to preetify the paras

        print(f"Company Name: {company_name.strip()}")
        print(f"Required Skills: {skills.strip()}")
        print(f"More Info: {more_info}")

        print('')

        # Now filter out things abd you follow the main.py file in Real-Website

        

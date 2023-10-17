from bs4 import BeautifulSoup

with open('./Basic-HTML-Scrapping/home.html', 'r') as html_file:
    content = html_file.read()
    #print(content)

    soup = BeautifulSoup(content, 'lxml')
    #print(soup.prettify())

    #tags = soup.find_all('h5')  #if only find tag is it will find only first tag
    #print(tags)

    #courses_html_tags = soup.find_all('h5')
    #for course in courses_html_tags:
     #   print(course.text)


     #Uncommit all the above and make them learn step wise
    course_cards = soup.find_all('div', class_='card')
    for course in course_cards:
        #print(course.a)
        course_name = course.h5.text
        #course_price = course.a.text #start with this firsat
        course_price = course.a.text.split()[-1]
        #print(course_name)   #This before
        #print(course_price)

        print(f'{course_name} costs {course_price}')
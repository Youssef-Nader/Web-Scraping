from bs4 import BeautifulSoup  # BeautifulSoup4 is a Python library for pulling data out of HTML and XML files
import requests  # Requests is a Python library for sending HTTP requests
import csv       # CSV (Comma Separated Values) is a simple file format used to store tabular data, such as a spreadsheet

page = requests.get("https://wuzzuf.net/search/jobs/?a=hpb&q=full%20stack%20engineer") # get the page url
src = page.content #get the content
soup = BeautifulSoup(src, 'lxml') # parse the page content using the lxml parser

# print(soup.prettify()) # print the parsed data of html
# list of each datails of jobs 
job_titles = []
company_names = []
locations = []
skills = []
# get the job title
job_title = soup.find_all("h2", class_="css-m604qf")  # find all the h2 with the class css-m604qf
# get the company name
company_name = soup.find_all("a", class_="css-17s97q8") # find all the a with the class css-17s97q8
# get the location
location = soup.find_all("span", class_="css-5wys0k") # find all the span with the class css-5wys0k
# get the skills
job_skills = soup.find_all("div", class_="css-y4udm8") # find all the div with the class css-y4udm8

#get all details of jobs in different lists with loop
for i in range(len(job_title)):
    job_titles.append(job_title[i].text)
    company_names.append(company_name[i].text)
    locations.append(location[i].text)
    skills.append(job_skills[i].text)

# write the data to a csv file
with open ("C:/Users/20128/desktop/Full-Stack Developer_jobs.csv", "w") as file:
    write = csv.writer(file) # create a csv writer object
    write.writerow(["Job Title", "Company Name", "Location", "Skills"])
    for i in range(len(job_titles)):
        write.writerow([job_titles[i], company_names[i], locations[i], skills[i]])

print("File created successfully") # print the message after the file created successfully
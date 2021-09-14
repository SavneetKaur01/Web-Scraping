import csv
import requests
from bs4 import BeautifulSoup 

temp='https://in.indeed.com/jobs?q={}&l={}'

def get_url(position,location):
    temp='https://in.indeed.com/jobs?q={}&l={}'
    url=temp.format(position,location)
    return url

url=get_url('software engineer', 'Bengaluru')

#Extract job description

response= requests.get(url)
print(response) #response 200 if request is successful

#to get html tree structure, use text attribute and navigate through it using parser object
soup= BeautifulSoup(response.text,'html.parser')

cards=soup.find_all("div", "job_seen_beacon")

print(len(cards))
recordlist=[]
for card in cards:
    title=card.find('h2').text.strip()
    print(title)
    company_tag= card.pre.span
    company_name=company_tag.text.strip()
    print(company_name)
    jobs=card.find('ul').text.strip()
    print(jobs)
    record={
        'title':title,
        'company':company_name,
        'Job Description':jobs
        }
    recordlist.append(record)
print(recordlist)
keys = recordlist[0].keys()
with open('jobs.csv', 'w', newline='')  as output_file:
    dict_writer = csv.DictWriter(output_file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(recordlist)
    
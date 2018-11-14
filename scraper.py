from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('https://boards.greenhouse.io/embed/job_board?for=birchbox&b=https%3A%2F%2Fwww.birchbox.com%2Fabout%2Fopenings')
soup = BeautifulSoup(html.read(), 'html.parser')

jobs = {}

def get_jobs():
    for department in soup.find_all(attrs={'class': 'level-0'}):
        for dep in department.find_all('h3'):
            jobs[dep.string] = []
            for el in department.find_all(attrs={'class': 'opening'}):
                try:
                    if dep.string in jobs:
                        jobs[dep.string].append(el.find('a').string)
                    else:
                        jobs[dep.string]=el.find('a').string
                except AttributeError:
                    pass
    
get_jobs()
print(jobs)
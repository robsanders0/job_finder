from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('https://boards.greenhouse.io/embed/job_board?for=birchbox&b=https%3A%2F%2Fwww.birchbox.com%2Fabout%2Fopenings')
soup = BeautifulSoup(html.read(), 'html.parser')


department_map = {10069: 'Birchbox Man'}
jobs = {}
job_list_test = []

#for button in soup.find_all(attrs={'class': 'opening'}):
    #print(button.prettify())
    
for department in soup.find_all(attrs={'class': 'level-0'}):
    for dep in department.find_all('h3'):
        for el in department.find_all(attrs={'class': 'opening'}):
            try:
                if dep.string in jobs:
                    jobs[dep.string].append(el.find('a').string)
                else:
                    jobs[dep.string]=el.find('a').string
            except AttributeError:
                pass
        
print(jobs)
#for x in jobs.items():
    #print (x)
    
import requests
from bs4 import BeautifulSoup 
import csv
from datetime import date

url = 'https://github.com/trending'
page = requests.get(url)
# print(page)

soup = BeautifulSoup(page.content, 'html.parser')
boxes = soup.find_all(class_='Box-row')


file_name = 'githubTrendingToday.csv'
file = csv.writer(open(file_name, 'w', newline=''))
file.writerow(['Developer', 'Repository name', 'Total stars', 'Stars Today ' + date.today().strftime("%b-%d-%Y")])


for box in boxes:    
    dev_repo_name = box.find(class_='h3 lh-condensed').find('a').text.split('/')
    developer = dev_repo_name[0].strip()
    repository_name = dev_repo_name[1].strip()
    
    total_stars = box.find(class_='f6 text-gray mt-2').find('a').text.strip()
    stars_today = box.find('span', {'class':'d-inline-block float-sm-right'}).text.strip()[:-12]
    """
    print(developer)
    print(repository_name)
    print(total_stars)
    print(stars_today)
    """
    file.writerow([developer, repository_name, total_stars, stars_today])
    

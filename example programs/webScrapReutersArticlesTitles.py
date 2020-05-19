import requests
from bs4 import BeautifulSoup
from csv import writer

response = requests.get("https://www.reuters.com")

soup = BeautifulSoup(response.text, 'html.parser')

articles = soup.find_all(class_='article-heading')
articles += soup.find_all(class_='story-title')
# articles += soup.find_all('li')

for article in articles:
    try:
        title = article.find('a').get_text().replace('\n', '')
    except:
        continue
    else:
        print(title)

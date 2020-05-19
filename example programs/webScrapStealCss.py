import requests
from bs4 import BeautifulSoup
from csv import writer

response = requests.get("https://www.reuters.com")

soup = BeautifulSoup(response.text, 'html.parser')

styles = soup.find_all('style')
cssStyles = list(map(lambda sub: sub.split('}'), styles))


# for style in styles:
#     try:
#         style = style.split("}")
#     except:
#         continue
#     else:
#         for i in style:
#             cssStyles += i

print(cssStyles)

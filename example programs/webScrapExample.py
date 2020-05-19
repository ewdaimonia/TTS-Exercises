import requests
from bs4 import BeautifulSoup
from csv import writer
# Eventually we will want a function which will take in params of the portfolio page url and the class name of the individual portfolio parent that will contain the <a> link within it
# Store and name associative arrays for each company, or custom objects?


# class WpDevPortfolio:
#     def __init__(self, portfolioUrl, wrapClass):
#         self.portfolioUrl = portfolioUrl
#         self.wrapClass = wrapClass


def main():
    # FBM = WpDevPortfolio("https://www.funnelboostmedia.net/client-portfolio/", 'jet-portfolio__content-inner')
    # BD = WpDevPortfolio("https://www.bensondesign.com/website-design/", )
    mainResponse = requests.get(
        "https://www.funnelboostmedia.net/client-portfolio/")

    mainSoup = BeautifulSoup(mainResponse.text, 'html.parser')
    websites = mainSoup.find_all(class_='jet-portfolio__content-inner')
    urls = []
    for website in websites:
        try:
            urls.append(website.find('a').get('href').replace('\n', ''))
        except:
            continue
    urls = list(dict.fromkeys(urls))

    # print(urls)
    for url in urls:
        miniResponse = requests.get(url)
        miniSoup = BeautifulSoup(miniResponse.text, 'html.parser')
        head = miniSoup.find('head')

        break


if __name__ == "__main__":
    main()

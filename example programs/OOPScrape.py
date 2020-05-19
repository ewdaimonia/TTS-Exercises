# This is a project by Gabriel Smith designed to take in the url of a wp web development website, find the portfolio page of the website
# and gather import information from the headers of all respective completed websites. The idea is to compare value of different wp companies
# relatively quickly, or to display the popularity of certain wp themes and plugins within a certain group of web development companies.

# Other ideas: approximate cost calculator based on number of pages and custom code / graphics
import requests
from bs4 import BeautifulSoup
from csv import writer


class WpDevAnalyzer:
    # Constructor which creates the soup object, the title of the main page, and initializes the folio attribute
    def __init__(self, url):
        self.url = url
        self.soup = BeautifulSoup(requests.get(url).text, 'html.parser')
        self.title = self.soup.title.string
        self.folio = "Not found"

    def findFolio(self):
        mainPageLinks = self.soup.findAll('a')
        self.folio = list(filter(lambda i: i if(
            i.getText() == "Our Work") else(i if(i.getText() == "Portfolio") else False), mainPageLinks))
        try:
            tempURL = self.folio[0].get('href')
            if('.net' not in tempURL and '.com' not in tempURL and '.org' not in tempURL):
                self.folio = self.url + tempURL
            else:
                self.folio = tempURL
        except Exception as e:
            print(f'No usable portfolio link found for {self.url}: {e}')


def main():
    # Sites with anti scraping set up: "https://www.bensondesign.com"
    sites = ["https://www.funnelboostmedia.net",
             "https://rainmandigital.com", "https://www.quacito.com"]
    wSSrc = list(map(WpDevAnalyzer, sites))
    # for i in wSSrc:
    #     print(i.title)
    #     i.findFolio()
    #     print(i.folio)
    print(wSSrc[1].title)
    wSSrc[1].findFolio()
    print(wSSrc[1].folio)


if __name__ == "__main__":
    main()

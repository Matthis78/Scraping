import requests
from bs4 import BeautifulSoup
import requests_cache
import itertools
import functools
requests_cache = requests_cache.install_cache('cache')

page = r'https://leagueoflegends.fandom.com/wiki/List_of_champions'


class IMDBScraper():
    def __init__(self, url):
        self.url = url
        self.page = requests.get(self.url)
        self.soup = BeautifulSoup(self.page.text, 'html.parser')


    def get_title(self):
        titre = self.soup.find('div', class_='sitenotice__header').find('h1').text
        print(titre)
        
    def get_link(self):
        link = self.soup.find('div', class_='dablink').text
        print(link)

    def get_description(self):
        description = self.soup.find('div', class_='mw-parser-output').find('p').text
        print(description)

    def get_content(self):
        content = self.soup.find('div', class_='toc').find('h2').text
        contents = self.soup.find('div', class_='toc').find('ul').find_all('li')
        print(content)
        for item in contents:
            content_text = item.find('span', class_="toctext").text
            print(content_text)


    def get_champions(self):
        sub_row = self.soup.find('table', class_='article-table').find('tbody').find_all('tr')
        del sub_row[0]
        for row in sub_row:
            if(row.find_all('td')[4].find('span') != None and row.find_all('td')[5].find('span') != None):
                champion = {
                    'Champion': row.find_all('td')[0]['data-sort-value'],
                    'Classes': row.find_all('td')[1]['data-sort-value'],
                    'Date': row.find_all('td')[2].text.replace('\n',''),
                    'Last Change': row.find_all('td')[3].find('a')['title'],
                    'Blue essence': row.find_all('td')[4].find('span').text,
                    'RP': row.find_all('td')[5].find('span').text,
                }
                print(champion)


    def get_reduction(self):
        title = self.soup.find('h3').find('span', class_=('mw-headline')).text
        exerpt = self.soup.find('dd').find('div', class_=('dablink')).text
        price = self.soup.dl.find_next('ul').find('li').text
        
        print(title,exerpt,price)

    def get_scrapped (self):
        scrapped = self.soup.find('span', {"id": "List_of_Scrapped_Champions"}).text
       
        print(scrapped)

    def get_scrapedChampion(self):
        ul= self.soup.find("div",class_="columntemplate").find("ul").find_all("li")
        for row in ul:
            title = row.find('a')["title"]
            print(title)

    def get_trivia(self):
        trivia = self.soup.find('span', {"id": "Trivia"}).text
        print(trivia)

    def get_urf(self):
        urf = self.soup.find('div', class_=('columntemplate')).find_next('h2').find_next('ul').find_all("li")
        for row in urf:
            subtitle = row.find('a')["title"]
            print(subtitle)

    

    def print_all(self):
        self.get_title()
        self.get_link()
        self.get_description()
        self.get_content()
        self.get_champions()
        self.get_reduction()
        self.get_scrapped()
        self.get_scrapedChampion()
        self.get_trivia()
        self.get_urf()
        

    

scraper = IMDBScraper(page).print_all()
print(scraper)
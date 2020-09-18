import pandas
from selenium import webdriver
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
import urllib.request
import json
import math
import csv

def parse_detail_page(page_url, year):
    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
    request = urllib.request.Request(page_url,headers={'User-Agent': user_agent})
    html = urllib.request.urlopen(request).read()
    soup = BeautifulSoup(html,'html.parser')

    main_post = soup.find('div',attrs={'class':'a-section mojo-body aok-relative'})
    title = main_post.find('h1',attrs={'class':'a-size-extra-large'}).text
    rollout = main_post.find('div', attrs = {'class': 'a-section a-spacing-none mojo-performance-summary-table'})
    categorycashboxes = rollout.find_all('span', attrs={'class': 'a-size-medium a-text-bold'})
    try:
        intl = categorycashboxes[1].find('span', attrs={'class':'money'}).text
        intl = intl.replace("$", "")
        intl = intl.replace(",", "")
        intl = int(intl)
    except:
        intl = 0
    try:
        total = categorycashboxes[2].find('span', attrs={'class':'money'}).text
        total = total.replace("$", "")
        total = total.replace(",", "")
        total = int(total)
    except:
        total = 0


    allTables = main_post.find('div',attrs={'class':'a-section a-spacing-none mojo-h-scroll releases-by-region-section'})
    tables = allTables.find_all("table", attrs = {'class':'a-bordered a-horizontal-stripes mojo-table releases-by-region'})
    regionList = []
    regionGrossList = []
    for table in tables:
        region = table.find('th', attrs = {'colspan': '4'}).text
        grossBoxes = table.find_all('td', attrs= {'class': 'a-text-right a-align-center'})[1::2]
        grosses = []
        for box in grossBoxes:
            try:
                gross = box.find('span', attrs = {'class':'money'}).text
                gross = gross.replace("$", "")
                gross = gross.replace(",", "")
                grosses.append(int(gross))
            except:
                grosses.append(0)
        totalGross = sum(grosses)
        regionList.append(region)
        regionGrossList.append(totalGross)

    usagross = 0
    eurgross = 0
    lagross = 0
    apgross = 0
    chinagross = 0
    try:
        usagross = regionGrossList[regionList.index('Domestic')]
    except:
        usagross = "no data"

    try:
        eurgross = regionGrossList[regionList.index('Europe, Middle East, and Africa')]
    except:
        eurgross = "no data"

    try:
        lagross = regionGrossList[regionList.index('Latin America')]
    except:
        lagross = "no data"

    try:
        apgross = regionGrossList[regionList.index('Asia Pacific')]
    except:
        apgross = "no data"

    try:
        chinagross = regionGrossList[regionList.index('China')]
    except:
        chinagross = "no data"

    post_data = {
        'title':title,
        'year':year,
        'All Intl': intl,
        'Total Gross': total,
        'USA':usagross,
        'Europe, Middle East, and Africa':eurgross,
        'Latin America':lagross,
        'Asia Pacific':apgross,
        'China':chinagross,
    }
    return post_data

extracted_records = []

for year in range(1977, 2021):
    print(year)
    stryear = str(year)
    url = "https://www.boxofficemojo.com/year/world/" + stryear + "/"
    headers = {'user-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.3'}
    request = urllib.request.Request(url,headers=headers)
    html = urllib.request.urlopen(request).read()

    soup = BeautifulSoup(html,'html.parser')
    main_table = soup.find("div",attrs={'id':'table'})
    links = main_table.find_all("a",class_="a-link-normal")

    for index, link in enumerate(links): 
        title = link.text
        url = link['href']

        if not url.startswith('http'):
            url = "https://www.boxofficemojo.com"+url 

        if index >= 6:
            extracted_records.append(parse_detail_page(url, year))


with open('data.json', 'w') as outfile:
    json.dump(extracted_records, outfile, indent=4)

with open('data.json') as json_file: 
    data = json.load(json_file) 
data_file = open('grossesbyregion.csv', 'w') 

csv_writer = csv.writer(data_file) 

count = 0
  
for movie in data: 
    if count == 0: 

        header = movie.keys() 
        csv_writer.writerow(header) 
        count += 1

    csv_writer.writerow(movie.values()) 
  
data_file.close()

import pandas as pd
from bs4 import BeautifulSoup as bs
from urllib import request

website = request.urlopen("https://www.ufc.com/rankings").read()
soup = bs(website, 'html.parser')

table = soup.find_all('div', attrs={'class': 'view-grouping'})

header_data = []
fighters = []
header = soup.find_all('div', class_='view-grouping-header')
rankings = soup.find_all('div', attrs={'class':'views-row'})

for res in header:
    header_data.append(res.text)
for each in fighters:
        fighters.append(each.find('a').text)

for tr in rankings:
    td = tr.find_all('a')
    row = [tr.text for tr in td]
    fighters.append(row)

df = pd.DataFrame(fighters, columns=header_data[1:])
df.to_csv('UfcRankings.csv')

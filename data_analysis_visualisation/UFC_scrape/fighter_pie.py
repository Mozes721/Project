from bs4 import BeautifulSoup as bs
from urllib import request
import matplotlib.pyplot as plt
import numpy as np
import re

webpage = request.urlopen('http://www.ufcstats.com/fighter-details/22a92d7f62195791').read()
soup = bs(webpage, 'html.parser')

fighter = soup.find('span', class_='b-content__title-highlight').text
fighter = fighter[15:]

record = soup.find('span', class_="b-content__title-record").get_text()


record = record[25:]
record = record.split('-')
wins = int(record[0])
losses = int(record[1])
draws = int(record[2])

####BAR PLOT###


bars = ['Wins', 'Losses', 'draws']

y_pos = np.arange(len(bars))

values = [wins, losses, draws]
plt.title(fighter)
plt.xticks(y_pos, bars)

plt.ylabel('Record')
plt.bar(y_pos, height=values, color=('g', 'r', 'b'))
#plt.show()

###PIE PLOT####

type_stats = []
stats_values = []

carrer_stats = soup.find_all('div', class_='b-list__info-box b-list__info-box_style_middle-width js-guide clearfix')[0].get_text().split("\n")


print(carrer_stats)
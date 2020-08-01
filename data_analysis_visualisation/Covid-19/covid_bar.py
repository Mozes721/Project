import requests
from bs4 import BeautifulSoup as bs
import numpy as np
import matplotlib.pyplot as plt

url = "https://www.worldometers.info/coronavirus/"
req = requests.get(url)
bsObj = bs(req.text, "html.parser")

data1 = bsObj.find_all("div", class_="panel-body")[0]
data2 = bsObj.find_all("div", class_="panel-body")[1]

def active(data):
    current_cases = data("div", class_="number-table-main")[0].text
    mild_condition = data("span", class_="number-table")[0].text
    serious_critical = data("span", class_="number-table")[1].text
    objects = ('Serious/Critcal', 'Mild conditions', 'Current Case')
    y_pos = np.arange(len(objects))
    situation = [serious_critical, mild_condition, current_cases]
    plt.bar(y_pos, situation, align='center', alpha=0.5, color = ('m', 'b', 'r'))
    plt.xticks(y_pos, objects)
    plt.ylabel('Population')
    plt.title('ACTIVE CASES')
    plt.show()


def closed(data):
    cases_with_outcome = data2("div", class_="number-table-main")[0].text
    recovered_dischared = data2("span", class_="number-table")[0].text
    deaths = data2("span", class_="number-table")[1].text

    objects = ('Deaths', 'Recovered/Dischared', 'Cases with outcome')
    y_pos = np.arange(len(objects))
    situation = [deaths, recovered_dischared, cases_with_outcome]
    plt.bar(y_pos, situation, align='center', alpha=0.5, color = ('m', 'b', 'r'))
    plt.xticks(y_pos, objects)
    plt.ylabel('Population')
    plt.title('CLOSED CASES')
    plt.show()



active(data1)
closed(data2)

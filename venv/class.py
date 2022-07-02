import requests
from bs4 import BeautifulSoup
import time
import csv

START_URL = 'https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars'
r = requests.get(START_URL)
# time.sleep(10)

def scrape():
    headers = ['name', 'distance', 'mass', 'radius']
    planet_data = []
    soup = BeautifulSoup(r.text, 'html.parser')
    for tr_tag in soup.find_all("tr"):
        td_tags = tr_tag.find_all('td')
        temp_list = []
        for index, td_tag in enumerate(td_tags):
            for i in range(0, len(td_tags)):
                if index == i:
                    temp_list.append(td_tag.text)
        planet_data.append(temp_list)
    planet_data.pop(0)
    for element_array in planet_data:
        for i in range(0, len(element_array)):
            element_array[i] = element_array[i].strip()
    for e in planet_data:
        del e[0]
        del e[1]
        del e[2]
        del e[4]

    with open('data.csv', 'w',encoding='utf-8') as f:
        csvwriter = csv.writer(f)
        csvwriter.writerow(headers)
        csvwriter.writerows(planet_data)

scrape()
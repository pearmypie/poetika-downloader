# Catană Ioan-Alexandru
# 28.03.2023

import requests
import time
from bs4 import BeautifulSoup

start_time = time.time()

site = "https://поэтика.рф"
url = "https://поэтика.рф/поэты/рыжий/сборники-стихов/все"

html = requests.get(url).content
data = BeautifulSoup(html, 'html.parser')

li_items = data.find_all('li', {'class': 'node-item'})

counter = 0
forbidden_characters = ['<', '>', ':', '"', '/', '\', '|', '?', '*']

for li in li_items:
    print("Starting!")

    total = len(li_items)

    for a in li.find_all('a'):
        poem_title = a.text.strip()
        href = a.get('href')
        poem_url = site + href
        
        for forbidden_character in forbidden_characters:
            poem_title = poem_title.replace(forbidden_character, '_')

        print("Downloading: " + poem_title)

        with open(f"{poem_title}.txt", "w", encoding='utf-8') as f:
            time.sleep(5)
            poem_html = requests.get(poem_url).content
            poem_data = BeautifulSoup(poem_html, 'html.parser')

            poem_div = poem_data.find('div', {'class': 'content clearfix'})

            try:
                paragraphs = poem_div.find_all('p')
                for p in paragraphs:
                    f.write(p.text.strip())
            except:
                print("Error: " + poem_title)
        
        counter += 1

        print("Done! " + str(counter) + " of " + str(total) + " poems downloaded.")

stop_time = time.time()
time_elapsed = stop_time - start_time

print("Finished!" + " Time elapsed: " + str(time_elapsed) + " seconds.")

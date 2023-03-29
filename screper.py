# Catană Ioan-Alexandru
# 28.03.2023

import requests
import time
import os
from bs4 import BeautifulSoup
from math import trunc


def main():
    start_time = time.time()

    try:
        sleep_time = float(input("Enter sleep time (seconds): "))
        author_name = input("Enter author name: ")
    except:
        print("Author name or sleep time is not valid!")
        return
    
    site = "https://поэтика.рф"
    url = f"https://поэтика.рф/поэты/{author_name}/сборники-стихов/все"

    if not os.path.exists(path):
        os.makedirs(path)

    html = requests.get(url).content
    data = BeautifulSoup(html, 'html.parser')

    li_items = data.find_all('li', {'class': 'node-item'})

    counter = 0
    forbidden_characters = ['<', '>', ':', '"', '/', '\\', '|', '?', '*'] # Windows forbidden characters

    for li in li_items:
        print("Starting!")
        total = len(li_items)

        if total > 500:
            print("Warning: more than 500 poems found! This may take a while.")
            print("Press Ctrl+C to stop the process.")
            _ = input("Press Enter to continue...")

        for a in li.find_all('a'):
            poem_title = a.text.strip()
            href = a.get('href')
            poem_url = site + href
            
            for forbidden_character in forbidden_characters:
                poem_title = poem_title.replace(forbidden_character, '_')

            print("Downloading: " + poem_title)

            with open(f"{author_name}\\{poem_title}.txt", "w", encoding='utf-8') as f:
                time.sleep(sleep_time)
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
            print("Done! " + str(counter) + " of " + str(total) + " poems downloaded (" + str(trunc((counter*100)/total)) + " % complete)")

    stop_time = time.time()
    time_elapsed = stop_time - start_time

    minutes, seconds = divmod(time_elapsed, 60)
    print("Finished!" + " Time elapsed: " + str(trunc(minutes)) + " minutes and " + str(trunc(seconds)) + " seconds.")
    print(f"{counter} poems downloaded from {author_name}.")


if __name__ == "__main__":
    main()
    input("Press Enter to exit...")

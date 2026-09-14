import requests
from bs4 import BeautifulSoup
import fake_useragent
import re
import multiprocessing
import os
import time

user = fake_useragent.UserAgent().random
HEADERS = {'user-agent': user}

start_page = 1
end_page = 5

os.makedirs('pictures', exist_ok=True)

#home_url = 'https://wallhaven.cc/'
link = f'https://wallhaven.cc/search?q=id%3A369&categories=110&purity=100&sorting=favorites&order=desc&page={start_page}'


responce = requests.get(link).text
soup = BeautifulSoup(responce, 'lxml')
block = soup.find('div', id="thumbs")

all_images = block.find_all('a', class_='preview')

image_links = []
for page in range(start_page, end_page + 1):
    link = f'https://wallhaven.cc/search?q=id%3A369&categories=110&purity=100&sorting=favorites&order=desc&page={page}'
    try:
        response = requests.get(link, headers=HEADERS, timeout=5).text
        soup = BeautifulSoup(response, 'lxml')
        block = soup.find('div', id="thumbs")
        if block:
            all_images = block.find_all('a', class_='preview')
            for image in all_images:
                image_links.append(image.get('href'))
    except requests.exceptions.RequestException:
        print(f" Страница {page} пропущена")


def get_direct_link(detail_url):
    try:
        response = requests.get(detail_url, headers=HEADERS, timeout = 5).text
        soup = BeautifulSoup(response, 'lxml')
        img_tag = soup.find('img', id='wallpaper')
        return img_tag.get('src') if img_tag else None
    except requests.exceptions.RequestException:
        return None

def download_image(img_url, img_name):
    response = requests.get(img_url, headers=HEADERS)
    with open(f'pictures/{img_name}', 'wb') as f:
        f.write(response.content)

for detail_url in image_links:
    img_url = get_direct_link(detail_url)
    if img_url:
        img_name = img_url.split('/')[-1]
        download_image(img_url, img_name)
        print(f"Скачано: {img_name}")


if __name__ == '__main__':
    image_links = []
    for page in range(start_page, end_page + 1):
        link = f'https://wallhaven.cc/search?q=id%3A369&categories=110&purity=100&sorting=favorites&order=desc&page={page}'
        try:
            response = requests.get(link, headers=HEADERS, timeout=5).text
            soup = BeautifulSoup(response, 'lxml')
            block = soup.find('div', id="thumbs")
            if block:
                all_images = block.find_all('a', class_='preview')
                for image in all_images:
                    image_links.append(image.get('href'))
        except requests.exceptions.RequestException:
            print(f"️ Страница {page} пропущена")
        time.sleep(1)

    tasks = []
    for detail_url in image_links:
        img_url = get_direct_link(detail_url)
        if img_url:
            img_name = img_url.split('/')[-1]
            tasks.append((img_url, img_name))

    with multiprocessing.Pool(multiprocessing.cpu_count()) as pool:
        pool.starmap(download_image, tasks)

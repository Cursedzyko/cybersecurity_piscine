import argparse
import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def download_img(img_url, save_path):
    try:
        response = requests.get(img_url, stream=True)
        response.raise_for_status()
        filename = os.path.join(save_path, img_url.split("/")[-1])
        with open(filename, 'wb') as file:
            for chunk in response.iter_content(1024):
                file.write(chunk)
        print(f"Downloaded: {filename}")
        
    except Exception as e:
        print(f"Failed to download {img_url} : {e} ")

def scrape_img(url, save_path):
    try:
        response = requests.get(url)
        response.raise_for_status()
        print(response)
        soup = BeautifulSoup(response.text, 'html.parser')

        print(soup.title.string)  
        for img_tag in soup.find_all('img'):
            # print(img_tag)
            img_url = img_tag.get('src')
            if img_url:
                img_url = urljoin(url, img_url)
                # print(img_url)
                if img_url.lower().endswith((".jpg", ".jpeg", ".png", ".gif", ".bmp")):
                    download_img(img_url, save_path)
                


    except Exception as e:
        print(f"Failed to proccess {url} : {e}!")

def main():
    parser = argparse.ArgumentParser(description="A Spider program to download pictures", usage="python spider url -r -l [L](depth level) -p [P](path)")
    parser.add_argument('url', help="Url to start scraping from")
    parser.add_argument('-r', action="store_true", help="Recursive download")
    parser.add_argument('-l', type=int, default=5, help="Max depth level for recursive download")
    parser.add_argument('-p', default="./data/", help="Path to save downloaded images")
    args = parser.parse_args()
    print(args)

    save_path = args.p

    print(save_path)
    os.makedirs(save_path, exist_ok=True)
    scrape_img(args.url, save_path)

if __name__ == "__main__":
    main()

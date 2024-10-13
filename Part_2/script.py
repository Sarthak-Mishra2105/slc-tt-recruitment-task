import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import re
from typing import List

base_url: str = "https://intranet.iiit.ac.in"

def get_intranet_links(file_extension: str) -> None:
    response = requests.get(base_url)
    soup = BeautifulSoup(response.content, 'html.parser')
    links = soup.find_all('a')
    urls: List[str] = []
    for link in links:
        url = link.get('href')
        if url is not None and url.endswith(file_extension) and not url.startswith("http"):
            urls.append(url)
    
    with open('urls.txt', 'w') as f:
        for url in urls:
            f.write(base_url + url + '\n')

def main() -> None:
    extension: str = input("Enter the file extension to search for: ")
    get_intranet_links(extension)

if __name__ == "__main__":
    main()
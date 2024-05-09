# scraper.py
import requests
from bs4 import BeautifulSoup

def scrape_images():
    # URL dari waifu.pics
    url = 'https://waifu.pics/api/sfw/waifu'
    
    # Mengambil konten HTML dari URL
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Menemukan tag <img> yang mengandung foto-foto
    image_tags = soup.find_all('img', class_='img-fluid')
    
    # Mengambil URL gambar
    image_urls = [img['src'] for img in image_tags]
    
    return image_urls

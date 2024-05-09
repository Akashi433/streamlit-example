from flask import Blueprint, request, jsonify, render_template
import requests
from bs4 import BeautifulSoup

pinterest_routes = Blueprint('pinterest_routes', __name__)

@pinterest_routes.route('/pinterest_scraper')
def pinterest_scraper():
    # Get the search query from the request parameters
    search_query = request.args.get('query')

    if not search_query:
        return jsonify({'error': 'Please provide a search query'})

    # URL of the Pinterest search page
    url = f'https://www.pinterest.com/search/pins/?q={search_query}'

    # Send a GET request to the URL
    response = requests.get(url)

    # Parse the HTML content
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find the elements containing the data you want to scrape
    pins = soup.find_all('div', class_='Pin')

    # Extract the information you need from the elements
    scraped_data = []
    for pin in pins:
        pin_data = {
            'title': pin.find('h3', class_='Pin__title').text,
            'image_url': pin.find('img', class_='PinImage').get('src')
        }
        scraped_data.append(pin_data)

    # Render template with scraped data
    return render_template('pinterest.html', data=scraped_data)
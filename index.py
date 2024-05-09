# app.py
from flask import Flask, render_template
from scraper import scrape_images

app = Flask(__name__)

@app.route('/')
def index():
    image_urls = scrape_images()
    return render_template('index.html', image_urls=image_urls)

if __name__ == '__main__':
    app.run(debug=True)

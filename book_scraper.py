# book_scraper.py
# http://book.coscrape.com

#pip install scrapy
import scrapy

class BookSpider(scrapy.Spider):
    name = 'bookspider'
    start_urls = ['http://books.toscrape.com']

    def parse(self, response):
        for article in response.css('article.product_pod'):
            yield {
                'price': article.css(".price_color::text")
            }



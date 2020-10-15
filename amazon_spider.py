import scrapy
import os
from scrapy.crawler import CrawlerProcess
import html2text
import urllib 

class AmazonSpider(scrapy.Spider):
    
    name = 'amazon_spider'
    download_delay = 20.0
    custom_settings = { 'FEEDS' : {'results.csv':{'format':'csv'}}}
    start_urls = ['https://www.amazon.com/s?k=web+scraping+books']
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
        'referer': 'https://www.amazon.com/s?k=web+scraping+books&ref=nb_sb_noss',
        'upgrade-insecure-requests': '1',
        'cache-control': 'no-cache',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36'
        }
        
    params = {
        "i": "aps",
        "k": "web scraping books",
        "ref": "nb_sb_noss",
        "url": "search-alias=aps"
    }
        
    try:
        os.remove('results.csv')
    except OSError:
        pass
        
    def parse(self,response):
    
        converter = html2text.HTML2Text()
        converter.ignore_links = True
        
        listings = response.xpath('//*[contains(@class,"sg-col-20-of-24 s-result-item s-asin")]')
        
        for book in listings:
            title = book.xpath('.//*[@class="a-size-medium a-color-base a-text-normal"]/text()').get()
            title = title.replace('\"','')         
            author = book.css('.sg-col-12-of-28 .a-color-secondary').get()
            author = converter.handle(author)
            author = author.replace('\n\n','')
            star_rating = book.xpath('.//span[@class="a-icon-alt"]/text()').get()
            book_format = book.xpath('.//a[@class="a-size-base a-link-normal a-text-bold"]/text()').get().strip()
            price = book.xpath('.//span[@class="a-offscreen"]/text()').get()
            cover_image = book.xpath('//div[@class="a-section aok-relative s-image-fixed-height"]/img/@src').get()
            items = {
                'title' : title,
                'author' : author,
                'star_rating' : star_rating,
                'book_format' : book_format,
                'price' : price,
                'cover_url' : cover_image
            }
            
            yield items
            
        # Go to next page if next page exists
        next_url = f"{start_urls}{urllib.parse.urlencode(params)}"
        if response.xpath('//li[@class="a-last"]/a/text()').get() == 'Next':
            yield response.follow(next_url,callback=self.parse,)
    
# main driver

if __name__ == "__main__" :
    process=CrawlerProcess()
    process.crawl(AmazonSpider)
    process.start()

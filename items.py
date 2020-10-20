import scrapy

class AmzItem(scrapy.Item):

    title = scrapy.Field()
    author = scrapy.Field()
    star_rating = scrapy.Field()
    book_format = scrapy.Field()
    price = scrapy.Field()
    cover_image = scrapy.Field()


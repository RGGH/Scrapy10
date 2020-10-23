# -*- coding: utf-8 -*-
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#|r|e|d|a|n|d|g|r|e|e|n|.|c|o|.|u|k|
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+

import scrapy

class AmzItem(scrapy.Item):

    title = scrapy.Field()
    author = scrapy.Field()
    star_rating = scrapy.Field()
    book_format = scrapy.Field()
    price = scrapy.Field()
    cover_image = scrapy.Field()
    ratings = scrapy.Field()


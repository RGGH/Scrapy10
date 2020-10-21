# -*- coding: utf-8 -*-
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#|r|e|d|a|n|d|g|r|e|e|n|.|c|o|.|u|k|
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+

import sys
import mysql.connector
from mysql.connector import errorcode
from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem
from scrapy.crawler import CrawlerProcess
     
class AmzPipeline(object):

    def __init__(self):
        self.create_conn()
        self.create_table()
    
    def create_conn(self):

        # Connect to DB
        try:
            self.conn = mysql.connector.connect(   
                                    user = 'user1',
                                    passwd = 'password1',
                                    host = 'localhost',
                                    port=3306,
                                    database ='amz'
            )
        except mysql.Error as e:
            print(f"Error connecting to DB Platform: {e}")
            sys.exit(1)
                                                             
        self.curr = self.conn.cursor()
     
    def create_table(self):
        self.curr.execute("""DROP TABLE IF EXISTS amzbooks""")
        self.curr.execute("""CREATE TABLE IF NOT EXISTS amzbooks (
            id INT AUTO_INCREMENT PRIMARY KEY,
            title VARCHAR(255) NOT NULL,
            author VARCHAR(255),
            star_rating VARCHAR(40),
            book_format VARCHAR(255),
            price DECIMAL(7,2),
            cover_image VARCHAR(255))
            """)
            
    def process_item(self,item,spider):
        
        # Drop anything that is NOT a paperback
        adapter = ItemAdapter(item)
        if adapter.get('book_format'):
            if adapter['book_format'] == 'Paperback':
                self.store_db(item)
            else:
                raise DropItem(f"Not a paperback book {item}")

    def store_db(self,item):
        myquery = """INSERT into amzbooks 
        (title, author,star_rating,book_format,price, cover_image) 
        values (%s,%s,%s,%s,%s,%s)
        """
        val=(
            item.get('title'),
            item.get('author'),
            item.get('star_rating'),
            item.get('book_format'),
            item.get('price'),
            item.get('cover_image')
            )
        self.curr.execute(myquery, val)
        self.conn.commit()
        
    def close_spider(self, spider):
        self.conn.close()
        

    
  
        
       
            
     

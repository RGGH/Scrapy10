# -*- coding: utf-8 -*-
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#|r|e|d|a|n|d|g|r|e|e|n|.|c|o|.|u|k|
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+

import sqlite3

from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem

class AmzPipeline(object):

    def __init__(self):
        self.create_conn()
        self.create_table()
    
    def create_conn(self):
        self.conn = sqlite3.connect("test.db")
        self.curr = self.conn.cursor()
        
    def create_table(self):
        self.curr.execute("""DROP TABLE IF EXISTS books_sqlite""")
        self.curr.execute("""create table books_sqlite (
            title text,
            author text,
            book_format text
            )""")
            
    def process_item(self,item,spider):
        self.store_db(item)
        adapter = ItemAdapter(item)
        if adapter.get('book_format'):
            if adapter['book_format'] == 'Paperback':
                return item
        else:
            raise DropItem(f"Not a paperback book {item}")
   
    def store_db(self,item):
        self.curr.execute("""INSERT into books_sqlite values(?,?,?)""",(
            item['title'],
            item['author'],
            item['book_format']
        ))
        self.conn.commit()
    
    
        
       
            
     

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
            star_rating text,
            book_format text,
            price text,
            cover_image text
            )""")
            
    def process_item(self,item,spider):
        
        adapter = ItemAdapter(item)
        if adapter.get('book_format'):
            if adapter['book_format'] == 'Paperback':
                self.store_db(item)
            else:
                raise DropItem(f"Not a paperback book {item}")
         
        
   
    def store_db(self,item):
        myquery = """INSERT into books_sqlite 
        (title, author,star_rating,book_format,price, cover_image) 
        values (?,?,?,?,?,?)
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

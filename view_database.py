import sqlite3

# Scrapy would try and run this otherwise!

if __name__ == "__main__":

    conn = sqlite3.connect('test.db')
    cur = conn.cursor()
    a = cur.execute("""select * from  books_sqlite """)  
    for rows in a.fetchall():
        print(rows)
    conn.close()

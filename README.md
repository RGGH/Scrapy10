# Scrapy 10
Amazon Scrapy Spider ('web scraping books')

## Includes pipelines / Sqlite3 (See Branch "DB-MySQL" the full MySQL version)

[Scrapy Item Pipeline ](https://docs.scrapy.org/en/latest/topics/item-pipeline.html)

Uses 'pipelines.py' to send output to sqlite db - also filters out books so that only "Paperback" format are saved to db.

I use `process_item` to identify only 'Paperback' books from our Amazon Search.

<p align="center">
  <img src="/images/pb1_LI.jpg">
</p>
<br>
<p align="center">
  <img src="/images/scrapy-amazon.PNG">
</p>

See: https://github.com/RGGH/Scrapy10/tree/DB-MySQL for the MySQL version

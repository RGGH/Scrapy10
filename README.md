# Scrapy 10
Amazon Scrapy Spider ('web scraping books')

<br>
<p align="center">
  <img src="/images/sm1.PNG">
</p>

## Includes pipelines / MySQL

[Scrapy Item Pipeline ](https://docs.scrapy.org/en/latest/topics/item-pipeline.html)

Uses 'pipelines.py' to send output to sqlite db - also filters out books so that only "Paperback" format are saved to db.

I use `process_item` to identify only 'Paperback' books from our Amazon Search.

<p align="center">
  <img src="/images/pb1_LI.jpg">
</p>
<br>
<p align="center">
  <img src="/images/phpmyadmin_screenshot-800w.png">
</p>

## Visualizing the data with Matplotlib
<br>
<p align="center">
  <img src="/images/Figure_1.png">
</p>


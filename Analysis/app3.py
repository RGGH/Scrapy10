# app.py - make a graph from MySQL data from Scrapy
import pymysql
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
sns.set()

# the query to get only titles with changed prices
query = '''select amzbooks2.* from 
                                    (select amzbooks2.*,
                                    lag(price) over (partition by title order by posted) as prev_price
                                    from amzbooks2) amzbooks2
                where prev_price <> price'''

# connect to db
dbcon = pymysql.connect("192.168.1.7","user1","password1","amz")

# generate the plot from dataframe (from MySQL - the scraped (stored) data)
def gen_plot():
    SQL_Query = pd.read_sql_query(query, dbcon)

    amz_data = pd.DataFrame(SQL_Query, columns=['id','title','price', 'prev_price'])
    print(amz_data)

    opacity = 0.6
    r1 = plt.bar(amz_data.index, amz_data['prev_price'], color = 'green', label = 'prev_price',alpha=opacity)
    r2 = plt.bar(amz_data.index, amz_data['price'], color = 'red', label = 'price',alpha=opacity)

    plt.title('Amazon.com "Web Scraping" Book Price Tracker')
    plt.xticks(amz_data.index, amz_data['title'],color = 'green',rotation = 10, horizontalalignment = 'right')    
    plt.ylabel('Price in $')
    plt.legend()
    plt.show()

# Main Driver
if __name__ == '__main__':

    # connect to db on the remote server (192.168.1.7 where scraped data is stored)
    dbcon
    try:
        gen_plot()
    except: 
        print('Error - unable to connect / convert the data - check connection and code')
    finally:
    # close connection 
        dbcon.close()

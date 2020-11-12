# app3.py - make a graph from MySQL data from Scrapy and MySQL
import pymysql
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
sns.set_context('talk')

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
    short_title = (amz_data['title'].str[:28])

    fig, ax = plt.subplots()
    x = np.arange(len(amz_data['id'])) 
    opacity = 0.4
    bar_width = 0.4

    ax.bar(x, amz_data['prev_price'],
            width=bar_width, label='price decrease', color='green',edgecolor='green',alpha=opacity)

    ax.bar(x, amz_data['price'] ,
            width=bar_width, label='price increase', color='red', edgecolor='green',alpha=opacity)

    # Fix the x-axes.
    ax.set_xticks(x + bar_width / 2)
    ax.set_xticklabels(short_title, rotation=20, ha='right')

    # Add legend.
    ax.legend()
    
    # Axis styling.
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.spines['bottom'].set_color('#DDDDDD')
    ax.tick_params(bottom=False, left=False)
    ax.set_axisbelow(True)
    ax.yaxis.grid(True, color='#EEEEEE')
    ax.xaxis.grid(False)
    
    # Add axis and chart labels.
    ax.set_xlabel('title', labelpad=15)
    ax.set_ylabel('price', labelpad=15)
    ax.set_title('Amazon Price Tracker - Web Scraping Books', fontsize=28, pad=15)
    
    plt.savefig('g.png')
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

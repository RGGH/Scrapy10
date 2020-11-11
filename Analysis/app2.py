# app2.py - make a graph from MySQL data from Scrapy and MySQL
# Conditional logic for colours of bars - work in progress!

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

    print(amz_data)

    fig, ax = plt.subplots()
    x = np.arange(len(amz_data['id']))
    # print(x)
    # print("\n")

    bar_width = 0.4

    # Note we add the `width` parameter now which sets the width of each bar.
    b1 = ax.bar(x, amz_data['price'] ,
            width=bar_width, label='price')

    values = amz_data['price']

    clrs = ['grey' if (x < max(values)) else 'red' for x in values ]

    # Same thing, but offset the x by the width of the bar.
    b2 = ax.bar(x + bar_width, amz_data['prev_price'],
            width=bar_width, label='prev_price', color=clrs)

    # Fix the x-axes.
    ax.set_xticks(x + bar_width / 2)
    ax.set_xticklabels(amz_data['title'])

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
    ax.set_title('Amazon Price Tracker', pad=15)
    
    #fig.tight_layout()
    fig.autofmt_xdate(rotation=20)
    #plt.grid(True)
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

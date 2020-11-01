# app.py - make a graph from MySQL data from Scrapy

import matplotlib.pyplot as plt
import pymysql
import pandas as pd
plt.style.use('ggplot')

# connect to db

dbcon = pymysql.connect("localhost","user1","password1","amz")

try:
    SQL_Query = pd.read_sql_query(
        '''SELECT star_rating, price FROM amzbooks2 WHERE star_rating > 1 ORDER BY price ASC''', dbcon 
    )

    df = pd.DataFrame(SQL_Query, columns=['star_rating','price'])
    print(df)

    df.plot.bar( x = 'price', y = 'star_rating', color="green")
    plt.ylabel('Rating')
    plt.xlabel('Price')
    plt.title("Ratings v Price - Amazon Books")
    plt.show()

except: 
    print("Error - unable to connect / convert the data - check connection and code")

dbcon.close()

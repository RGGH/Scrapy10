# app.py
import matplotlib.pyplot as plt
import pymysql
import pandas as pd

# connect to db
dbcon = pymysql.connect("localhost", "user1", "password1", "amz")

try:
    SQL_Query = pd.read_sql_query(
        '''select
        author,
        title,
        price
        from amzbooks''',dbcon)

    df = pd.DataFrame(SQL_Query, columns=['star_rating', 'title', 'price'])
    print(df)
    print('The data type of df is: ', type(df))
   

except:
    print("Error: unable to convert the data - check your code")


    
dbcon.close()

# work in progress
df.plot(x="star_rating", y="price")
plt.show()

"""
Ingerstion data the set50 index stock price to loading area.

"""
import pandas as pd
import sqlite3

from pandas_datareader import data
from sqlite import Sqlite

# sqlite db
sqlite = Sqlite()
# constans
SET50 = '^SET50.BK'
SOURCE = 'yahoo'
# go get data
set50_df = data.DataReader(SET50, data_source=SOURCE)
# create an empty list
set50_list = []
# iterate over the rows
for idx, row in set50_df.iterrows():
    # create a dictionary with the set50
    data = {'date_': idx.strftime("%Y-%m-%d"), 'high': row[0], 'low': row[1], 'open': row[2], 'close': row[3],
            'volume': row[4], 'adj_close': row[5]}
    # append to the set50 list
    set50_list.append(data)
# create table for data
create_db = sqlite.create_set50()
# use set50_list to insert data
insert_db = sqlite.insert_set50(set50_list)
# get set50_index
select_db = sqlite.select_set50()
if __name__ == '__main__':
    print('set50 today: {}'.format(set50_list))
    pass

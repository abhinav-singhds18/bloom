import pyodbc
import json
import pandas as pd



conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=ABHINAV-UG1-330;'
                      'Database=test_db;'
                      'Trusted_Connection=yes;')

cursor = conn.cursor()
print(cursor)

cursor.execute('SELECT * FROM tsdata')
for row in cursor:
    print(row)

with open('response.txt') as json_file:
    datawr = json.load(json_file)
    #print(data)
    print(type(datawr))
    df = pd.DataFrame(datawr)
    print(df)
    print(datawr['dataset_data']['data'])


# sql = "INSERT INTO tsdata VALUES (?, ? ,?,?,?,?,?,?,?,?,?,?,?)"
#
# number_of_rows = cursor.executemany(sql, datawr['dataset_data']['data'])
#
# conn.commit()
# cursor.execute('''DECLARE @json NVARCHAR(MAX)
# SET @json =   %s
#
# SELECT * FROM
#  OPENJSON ( @json )
# WITH (
#               Number   varchar(200) '$.Order.Number' ,
#               Date     datetime     '$.Order.Date',
#               Customer varchar(200) '$.AccountNumber',
#               Quantity int          '$.Item.Quantity'
#  ) ''', data['dataset_data']['data'])

fields = datawr['dataset_data']['column_names']
values = datawr['dataset_data']['data']

cursor.execute('''
 declare @json nvarchar(max) = 'values';

''')


# for row in cursor:
#     print(row)

for drivers in pyodbc.drivers():
    print(drivers)

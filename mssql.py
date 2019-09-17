import pyodbc
import json



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
    print(datawr['dataset_data']['data'])


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



'''
Created on 24-Apr-2018

@author: Appu
'''
import MySQLdb

# Open database connection
db = MySQLdb.connect("localhost","root","","alldatacheck" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

# execute SQL query using execute() method.
cursor.execute("SELECT VERSION()")

# Fetch a single row using fetchone() method.
data = cursor.fetchone()
print('Database version : , %s' % data)

# disconnect from server
db.close()
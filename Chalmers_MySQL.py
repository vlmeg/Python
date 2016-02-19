import MySQLdb

db = MySQLdb.connect(host="db.student.chalmers.se", # your host, usually localhost
                     user="vlasios", # your username
                      passwd="******", # your password
                      db="vlasios") # name of the data base

# you must create a Cursor object. It will let
#  you execute all the queries you need
cur = db.cursor() 

# Use all the SQL you like
cur.execute("SELECT * FROM *")

# print all the first cell of all the rows
for row in cur.fetchall() :
    print row[0]
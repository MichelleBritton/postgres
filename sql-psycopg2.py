import psycopg2

# connnect to "chinnok" database, we coujld add additionalk connection values such as host, username and password but
# since we are working locally and haven't set up any credentials we only need the database name
connection = psycopg2.connect(database="chinook")

# build a cursor object of the database. A cursor object is another way of saying a set or list, similar to an array in JS
# Essentially anything we query from the database will become part of the cursor object and to read that data we should iterate
# over the cursory using a for- loop, as an example.  Before we start to query the dtabases, we need to set up a way for our data to be retrieved from the cursor
cursor = connection.cursor()

# Query 1 - select all records from teh "Artist" table
# cursor.execute('SELECT * FROM "Artist"')

# Query 2 - Select only the "Name" column from the "Artist" table
# cursor.execute('SELECT "Name" FROM "Artist"')

# Query 3 - Select only the "Queen" from the "Artist" table. %s is a python string placeholder and then define desired string within a list
# Technically since we know there should only be one result we could use the fetchone() method.
#cursor.execute('SELECT * FROM "Artist" WHERE "Name" = %s', ["Queen"])

# Query 4 - Select only by "ArtistId" #51 from the "Artist" table. 
#cursor.execute('SELECT * FROM "Artist" WHERE "ArtistId" = %s', [51])

# Query 5 - Select only the albums with "ArtistId" #51 from the "Album" table. 
#cursor.execute('SELECT * FROM "Album" WHERE "ArtistId" = %s', [51])

# Query 6 - Select all tracks where the composer is "Queen" from the track table
cursor.execute('SELECT * FROM "Track" WHERE "Composer" = %s', ["Queen"])

# fetch the results (multiple)
results = cursor.fetchall()

# feth the results (single)
#results = cursor.fetchone()

# close the connection
connection.close()

#  print results. In order to retreive each record individually we need to iterate over the results using a for loop
for result in results:
    print(result)



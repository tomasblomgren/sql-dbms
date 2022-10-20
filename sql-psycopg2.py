import psycopg2


# connect to "chinook" database
connection = psycopg2.connect(database="chinook")


# Query 1 - SELECT all records from the "Artist" table
cursor.execute('SELECT * FROM "Artist"')


# build a cursor object of the database
cursor = connection.cursor()

# fetch the results (multiple)
results = cursor.fetchall


# fetch the results (single)
# results = cursor.fetchone


# close the connection
connection.close()

# print results
for results in results:
    print(results)

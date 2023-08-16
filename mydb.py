import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = '',

)

# create a curson object
cursorObject = dataBase.cursor()

# Create a database
cursorObject.execute("CREATE DATABASE  balucrm")

print("all Done")
import mysql.connector

mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'Admin',
    password = 'pamisolo97*',
    database = 'Facial_Recognition'
)
cursor = mydb.cursor()
query = 'CREATE TABLE user '



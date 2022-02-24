import mysql.connector as connector

dbConnection = connector.connect(
    host = 'localhost',
    user = 'root',
    password='Token2021',
    database='schoolDb'
)
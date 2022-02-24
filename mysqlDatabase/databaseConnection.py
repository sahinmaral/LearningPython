import mysql.connector as connector


dbConnection = connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'Token2021',
    database = 'northwind'
)

dbCursor = dbConnection.cursor()
# databaseCursor.execute("CREATE TABLE `testTable` (`name` VARCHAR(50),`desc` VARCHAR(50))")

# databaseCursor.execute('SELECT * FROM customers')

# for x in databaseCursor:
#     print(x)

def updateProduct(dbCursor,dbConnection):
    query = "UPDATE test SET productName='Nice Lamp' WHERE productName='Lamp'"
    dbCursor.execute(query)

    try:
        dbConnection.commit()
        
    except connector.Error as err:
        print('hata : ',err)
    finally:
        dbConnection.close()

updateProduct(dbCursor,dbConnection)





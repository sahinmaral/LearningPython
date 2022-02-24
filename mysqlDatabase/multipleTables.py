import mysql.connector as connector


dbConnection = connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'Token2021',
    database = 'northwind'
)

dbCursor = dbConnection.cursor()

def getProducts(dbCursor):
    query = 'SELECT pd.id , pd.productName ,pd.price, ct.name FROM test_products pd INNER JOIN test_categories ct ON pd.categoryId = ct.id'
    dbCursor.execute(query)

    products = dbCursor.fetchall()

    for product in products:
        print(product)

getProducts(dbCursor)
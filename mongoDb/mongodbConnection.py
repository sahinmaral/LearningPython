import pymongo
from bson.objectid import ObjectId

myClient = pymongo.MongoClient('mongodb+srv://sahinmaral:jboNR7Ahh0NXPZaP@cluster0.c0mpc.mongodb.net/node-app?retryWrites=true&w=majority')

myDb = myClient['node-app']
productCollection = myDb['products']

# Insert -> Tekil veri yollamak icin
def insertSingle():
    product = {'name':'Samsung S5' , 'price' : 2000}
    result = productCollection.insert_one(product)
    print(result)
    print(type(result))

    print(myClient.list_database_names())


# Insert -> Coklu veri yollamak icin
def insertMany():
    productList = [
        {'name':'Samsung S5 Lite' , 'price' : 3000},
        {'name':'Samsung S6' , 'price' : 4000},
        {'name':'Samsung S7' , 'price' : 5000},
        {'name':'Samsung S8' , 'price' : 6000},
    ]

    result = productCollection.insert_many(productList)
    print(result.inserted_ids)

def findOne():
    result = productCollection.find_one()
    print(result)

# Select -> Butun kayitlari getirir
def getProducts():
    # Birinci parametresi : query
    # Ikinci parametresi : gelmesini istedigimiz kolonlar (0 gelmemesini istedigimiz alana yazilir)
    # result = productCollection.find({},{'_id':0}).sort('price',-1)  # -1 -> DESC
    result = productCollection.find({},{'_id':0}).sort([('price',-1),('name',1)])
    for i in result:
        print(i)

def getProductById():
    # filter = {'name':'Samsung S5'}
    
    result = productCollection.find_one({'_id':ObjectId('621824f0ec9f88388e426e8d')})
    print(result)
    

def getProductsFilter():
    # Birinci parametresi : query
    # Ikinci parametresi : gelmesini istedigimiz kolonlar (0 gelmemesini istedigimiz alana yazilir)
    # filter = {'name':{'$in':['Samsung S5','Samsung S6']}}
    # filter = {'price':{'$gte':2000}}
    # filter = {'price':{'$lt':2000}}
    # filter = {'name':{'$regex':'^S'}}
    
    result = productCollection.find(filter,{})
    for i in result:
        print(i)


# UPDATE -> Yapilan sorguda eslesen ilk satiri gunceller
def updateOne():
    productCollection.update_one(
        {'name':'Samsung S5'},
        {'$set':{
            'price':2500
        }}
        )


def updateMany():
    query = { "name": { "$regex": "Samsung" } }
    
    productCollection.update_many(
        query,
            {'$inc':{'price':500}}
        )

    getProducts()

# set ve inc komutlari ayni anda calisamaz cunku
# ikisi da farkli transaction olaylaridir

def addAnotherColumn():

    query = { "name": { "$regex": "Samsung" } }
    
    result = productCollection.update_many(
        query, 
            {'$set':{'description':'Guzel telefon'}} 
        )

    # Update sonrasi guncellenen nesnelerin sayisini getirir
    print(f'{result.modified_count}') 
    
    getProducts()

# Delete 
def deleteSomething():
    query = {'name':{'$regex':'Samsung S8'}}

    result = productCollection.delete_one(query)

    # Delete sonrasi silinen nesnelerin sayisini getirir
    print(result.deleted_count) 

    getProducts()

deleteSomething()
            
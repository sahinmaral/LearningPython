# Workbench IDE ile schooldb isminde bir database olusturup Student tablosunu ekleyiniz
# ID , StudentNumber , Name , Surname , Birthdate , Gender

# Database baglantisini olusturunuz

import mysql.connector as connector

# dbConnection = connector.connect(
#     host = 'localhost',
#     user = 'root',
#     password = 'Token2021'
# )

# dbCursor = dbConnection.cursor()
# dbCursor.execute('CREATE DATABASE schooldb')
# dbCursor.close()
# dbConnection.close()

dbConnection = connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'Token2021',
    database = 'schooldb'
)

dbCursor = dbConnection.cursor()

list = [
    (101,'Ahmet','Yilmaz','2005/05/17','M'),
    (102,'Ali','Can','2005/06/17','M'),
    (103,'Canan','Tan','2005/07/07','M'),
    (104,'Ayse','Taner','2005/09/23','F'),
    (105,'Bahadir','Toksoz','2004/07/27','M'),
    (106,'Ali','Cenk','2003/08/25','M')
]

# createStudentQuery = f"CREATE TABLE `student` (`id` int(11) NOT NULL AUTO_INCREMENT,`studentNumber` int(5), `name` varchar(20) , `surname` varchar(20) , `birthDate` date , `gender` enum('M','F') NOT NULL ,PRIMARY KEY (`id`)) ENGINE=InnoDB"

# dbCursor.execute(createStudentQuery)
# cursor.rowCount       eklenen kayit sayisi
# cursor.lastrowid      son kayitin id si

def insertStudents(dbCursor,list):
    insertStudentQuery= "INSERT INTO student(`studentNumber`,`name`,`surname`,`birthDate`,`gender`) VALUES(%s,%s,%s,%s,%s)"

    dbCursor.executemany(insertStudentQuery,list)
    try:
        dbConnection.commit()
        
        
    except connector.Error as err:
        print('hata : ',err)
    finally:
        dbConnection.close()


def getStudentsOrderByBirthdate(dbCursor):
    dbCursor.execute('SELECT name,surname,birthdate FROM student ORDER BY birthdate DESC')
    
    #birden fazla kayit dondurur
    students = dbCursor.fetchall()  
    
    # dbCursor.fetchone()               tek kayit dondurur

    for student in students:
        print(student)

def getStudentById(dbCursor,id):
    params = (id,)
    query = 'SELECT * FROM student where id = %s'
    dbCursor.execute(query,params)
    
    student = dbCursor.fetchone()  
    print(student)

def getStudents(dbCursor):
    query = 'SELECT * FROM student'
    dbCursor.execute(query)
    
    students = dbCursor.fetchall()  
    for student in students:
        print(student)

def getStudentsOnlyStudentNumberNameSurname(dbCursor):
    query = 'SELECT studentNumber,name,surname FROM student'
    dbCursor.execute(query)
    
    students = dbCursor.fetchall()  
    for student in students:
        print(student)

def getFemaleStudentsOnlyNameSurname(dbCursor):
    query = 'SELECT name,surname FROM student WHERE gender = "F"'
    dbCursor.execute(query)
    
    students = dbCursor.fetchall()  
    for student in students:
        print(student)

def getStudentsWhereBirthYear2003(dbCursor):
    query = 'SELECT * FROM student WHERE YEAR(birthdate)=2003'
    dbCursor.execute(query)
    
    students = dbCursor.fetchall()  
    for student in students:
        print(student)

def getStudentsWhereNameAliAndBirthYear2005(dbCursor):
    query = 'SELECT * FROM student WHERE YEAR(birthdate)=2005 AND name = "Ali"'
    dbCursor.execute(query)
    
    students = dbCursor.fetchall()  
    for student in students:
        print(student)

def getStudentsWhereNameSurnameIncludesAn(dbCursor):
    query = "SELECT * FROM student WHERE name OR surname LIKE '%an%'"
    dbCursor.execute(query)
    
    students = dbCursor.fetchall()  
    for student in students:
        print(student)

def getManStudentCount(dbCursor):
    query = 'SELECT COUNT(*) FROM student WHERE gender = "M"'
    dbCursor.execute(query)
    
    count = dbCursor.fetchone()  
    print(f'Erkek sayisi : {count}')

def getWomanStudentsOrderByName(dbCursor):
    query = 'SELECT * FROM student WHERE gender = "F" ORDER BY name,surname  '
    dbCursor.execute(query)
    
    students = dbCursor.fetchall()  
    for student in students:
        print(student)

# insertStudents(dbCursor,list)
# getStudentsOrderByBirthdate(dbCursor)
# getStudentById(dbCursor,3)

'''
Asagidaki sorgulari yaziniz
Tum ogrenci kayitlarini yaziniz
Tum ogrencilerin sadece ogrenci no,ad ve soyad bilgilerini yaziniz
Sadece kiz ogrencilerin ad ve soyadlarini aliniz
2003 dogumlu ogrenci bilgilerini aliniz
Ismi Ali ve dogum tarihi 2005 olan ogrenci bilgilerini aliniz
Ad veya soyadi icinde 'an' ifadesi gecen kayitlari aliniz
Kac erkek ogrenci vardir
Kiz ogrencileri harf sirasina gore getiriniz

'''

getStudents(dbCursor)
getStudentsOnlyStudentNumberNameSurname(dbCursor)
getFemaleStudentsOnlyNameSurname(dbCursor)
getStudentsWhereBirthYear2003(dbCursor)
getStudentsWhereNameAliAndBirthYear2005(dbCursor)
getStudentsWhereNameSurnameIncludesAn(dbCursor)
getManStudentCount(dbCursor)
getWomanStudentsOrderByName(dbCursor)


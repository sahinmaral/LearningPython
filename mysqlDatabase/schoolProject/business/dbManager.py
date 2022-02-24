import mysql.connector as Connector
import sys
sys.path.append('..')

from schoolProject.dataAccess.dbContext import dbConnection
from schoolProject.models.student import Student
from schoolProject.models.teacher import Teacher
from schoolProject.models.classEntity import Class
from schoolProject.models.classLesson import ClassLesson

class DbManager:
    def __init__(self):
        self.dbConnection = dbConnection
        self.cursor = self.dbConnection.cursor()

    def __del__(self):
        self.dbConnection.close()

    def addStudent(self,student:Student):
        query = 'INSERT INTO students (studentNumber,name,surname,gender,birthDate,classId) VALUES (%s,%s,%s,%s,%s,%s)'
        params = (student.studentNumber,student.name,student.surname,student.gender,student.birthDate,student.classId)

        self.cursor.execute(query,params)
        try:
            self.dbConnection.commit()
        except Connector.Error as err:
            print(err)

    def updateStudent(self,student:Student):
        query = 'UPDATE students SET studentNumber = %s ,name = %s ,surname = %s ,gender = %s ,birthDate = %s,classId = %s WHERE id=%s'
        params = (student.studentNumber,student.name,student.surname,student.gender,student.birthDate,student.classId,student.id)

        self.cursor.execute(query,params)
        try:
            self.dbConnection.commit()
        except Connector.Error as err:
            print(err)

    def addOrUpdateStudent(self,student:Student):
        if student.id == 0:
            self.addStudent(student)
        else:
            self.updateStudent(student)

    def deleteStudent(self,student:Student):
        query = 'DELETE FROM students WHERE id=%s'
        params = (student.id,)

        self.cursor.execute(query,params)
        try:
            self.dbConnection.commit()
        except Connector.Error as err:
            print(err)

    def getStudentById(self,id):
        query = 'SELECT * FROM students where id = %s'
        params = (id,)
        self.cursor.execute(query,params)

        try:
            student = self.cursor.fetchone()
            return Student.createStudent(student)
        except Connector.Error as err:
            print(err)

    def getStudents(self):
        query = 'SELECT * FROM students'
        self.cursor.execute(query)

        students = self.cursor.fetchall()
        return Student.createStudent(students)

    def getClassByClassName(self,name):

        query = "SELECT * FROM classes WHERE name LIKE '%"+str(name)+"%' "
        self.cursor.execute(query)

        foundClass = self.cursor.fetchone()
        return Class.createClass(foundClass)

    def getLessonsDetails(self):
        query = 'SELECT clls.id , cl.name , tc.name , ls.name  FROM classLessons clls INNER JOIN classes cl ON clls.classId = cl.id INNER JOIN teachers tc ON clls.teacherId = tc.id INNER JOIN lessons ls ON clls.lessonId = ls.id'

        self.cursor.execute(query)

        classLessons = self.cursor.fetchall()
        return classLessons

    def getStudentsByClassId(self,classId):
        query = 'SELECT * FROM students where classId = %s'
        params = (classId,)
        self.cursor.execute(query,params)

        try:
            students = self.cursor.fetchall()
            return Student.createStudent(students)
            
            
        except Connector.Error as err:
            print(err)




# db = DbManager()
# foundClass = db.getClassByClassName('10/A')
# print(foundClass[0].name)
# student = db.getStudentById(1)
# print(student[0].name,student[0].surname)

# student = Student(4,1126,'Veysel','Karaman','E','2004/11/02',2)
# student = Student(None,1300,'Hakki','Kesik','E','2004/04/02',1)
# db.addOrUpdateStudent(student)

# student = db.getStudentById(1)
# db.deleteStudent(student[0])

# students = db.getStudentsByClassId(1)
# for student in students:
#     print(student.studentNumber,student.name,student.surname)

# student = Student(None,1124,'Veysel','Karaman','E','2004/11/02',2)
# db.addStudent(student)


import sys
sys.path.append('..')

from schoolProject.business.dbManager import DbManager
from schoolProject.models.student import Student
from schoolProject.models.teacher import Teacher

class App:
    def __init__(self):
        self.db=DbManager()

    def getStudents(self):
        return self.db.getStudents()

    def getStudentById(self,id):
        return self.db.getStudentById(id)[0]

    def getClassByClassName(self,name):
        return self.db.getClassByClassName(name)[0]
    
    def addOrUpdateStudent(self):
        id = int(input('Ogrenci ID : (Eger yeni ekleyecekseniz 0 yaziniz) : '))
        name = input('Ogrenci adi : ')
        surname = input('Ogrenci soyadi : ')
        studentNumber = input('Ogrenci numarasi : ')
        gender = input('Ogrenci cinsiyeti (E,K) : ')
        birthDate = input('Ogrenci dogum tarihi (yil/ay/gun) : ')
        className = input('Ogrencinin sinifi : ')
        foundClass = self.getClassByClassName(className)
        
        student = Student(id,studentNumber,name,surname,gender,birthDate,foundClass.id)
        self.db.addOrUpdateStudent(student)
        
        if id == 0: print('Ogrenci eklendi')
        else: print('Ogrenci guncellendi')
    
    def deleteStudent(self):
        id = int(input('Ogrenci ID : '))
        student = self.getStudentById(id)
        self.db.deleteStudent(student)

        print('Ogrenci silindi')

    def addTeacher(self,teacher:Teacher):
        id = int(input('Ogretmen ID : (Eger yeni ekleyecekseniz 0 yaziniz) : '))
        name = input('Ogretmen adi : ')
        surname = input('Ogretmen soyadi : ')
        gender = input('Ogretmen cinsiyeti (E,K) : ')
        birthDate = input('Ogretmen dogum tarihi (yil/ay/gun) : ')
        branch = input('Ogretmenin bransi : ')
        
        teacher = Teacher(id,name,surname,branch,gender,birthDate)
        self.db.addTeacher(teacher)  

        if id == 0: print('Ogretmen eklendi')
        else: print('Ogretmen guncellendi')

    def initApp(self):
        message = '********** \n 1. Ogrenci Listesi \n 2. Ogrenci Ekle \n 3. Ogrenci Guncelle \n 4. Ogrenci Sil \n 5. Ogretmen Ekle \n 6. Siniflara Gore Dersler \n 7. Cikis'
        
        while True:
            print(message)
            process = int(input('Seciminiz : '))
            match process:
                case 1:  
                    students = self.getStudents()
                    for student in students:
                        print(student.id,student.studentNumber,student.name,student.surname,student.gender,student.birthDate,student.classId)
                case 2 :
                    self.addOrUpdateStudent()
                case 3:
                    self.addOrUpdateStudent()
                case 4:
                    self.deleteStudent()
                case 5:
                    self.addTeacher()
                case 6:
                    objects = self.db.getLessonsDetails()
                    for obj in objects:
                        print(obj)
                case 7:
                    exit()

app = App()
app.initApp()
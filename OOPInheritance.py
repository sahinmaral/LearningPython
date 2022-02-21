class User:
    def __init__(self,username,password):
        self.username = username
        self.password = password
    def whoAmI():
        print('I am user')


class Customer(User):
    def __init__(self, username, password,name,surname):
        super().__init__(username, password)
        self.name = name
        self.surname = surname
    
    # Kalitimli sinif icerisinde metot tanimlarken
    # parametreler icerisine self yazilmasi gerekir
    def whoAmI(self):
        print('I am customer')
    
    def testMethod(self):
        print('test method')

    def __str__(self) -> str:
        return (f'Adiniz : {self.name} , soyadiniz : {self.surname}')

    # def __init__(self, username, password):
    #     User.__init__(username, password)

customer1 = Customer('sahinmaral','1234','Sahin','MARAL')
print(customer1.name)
print(customer1.surname)
print(customer1.username)
print(customer1.password)
customer1.whoAmI()
customer1.testMethod()
print(str(customer1))


class Teacher:
    
    
    def __init__(self,id,name,surname,branch,gender,birthDate):
        if id is None: 
            self.id = 0
        else:
            self.id = id
        self.name = name
        self.surname = surname
        self.branch = branch
        self.gender = gender
        self.birthDate = birthDate
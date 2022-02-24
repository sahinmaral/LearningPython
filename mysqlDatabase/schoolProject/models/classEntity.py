class Class:
    
    
    def __init__(self,id,name,teacherId):
        if id is None: 
            self.id = 0
        else:
            self.id = id
        self.name = name
        self.teacherId = teacherId

    @staticmethod
    def createClass(obj):
        list = []
        if isinstance(obj,tuple):
            list.append(Class(obj[0],obj[1],obj[2]))
        else:
            for i in obj:
                list.append(Class(i[0],i[1],i[2]))
        return list
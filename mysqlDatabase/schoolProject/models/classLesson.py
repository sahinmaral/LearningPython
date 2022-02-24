class ClassLesson:
    
    
    def __init__(self,id,lessonId,teacherId,classId):
        if id is None: 
            self.id = 0
        else:
            self.id = id
        self.lessonId = lessonId
        self.teacherId = teacherId
        self.classId = classId

    @staticmethod
    def createClassLesson(obj):
        list = []
        if isinstance(obj,tuple):
            list.append(ClassLesson(obj[0],obj[1],obj[2]))
        else:
            for i in obj:
                list.append(ClassLesson(i[0],i[1],i[2]))
        return list
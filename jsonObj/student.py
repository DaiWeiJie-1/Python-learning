class Student(object):
    def __init__(self,name,age,size):
        self.name = name
        self.age = age
        self.size = size

    
    def student2dict(self):
        return {
            'name':self.name,
            'age':self.age,
            'size':self.size
        }


    def dict2student(d):
        return Student(d['name'],d['age'],d['size'])
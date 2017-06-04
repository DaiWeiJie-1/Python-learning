class Student(object):
    
    def __init__(self,name,score):
        self.__name = name
        self.__score = score

    def name1(self):
        return self.__name

    def score1(self):
        return self.__score

    def __age__(self):
        return 25

    
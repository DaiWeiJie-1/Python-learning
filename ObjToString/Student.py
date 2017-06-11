class Student(object):
    def __init__(self,name,age):
        self._name = name
        self._age = age

    def age(self):
        return self._age

    def name(self):
        return self._name

    def __str__(self):
        return 'Student class : name = %s,age = %d' % (self._name,self._age)


def main():
    s = Student('dwj',18)
    print(s)

if __name__ == '__main__':
    main()
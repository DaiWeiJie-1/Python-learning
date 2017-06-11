class Student(object):
    __slots__ = ('name','age','score','set_score','_addr')

    def __init__(self, name, age):
        self.name = name
        self.age = age


    @property
    def addr(self):
        return self._addr

    @addr.setter
    def addr(self,value):
        if not isinstance(value,str):
            raise ValueError('addr must be str')
        self._addr = value
from Student import Student
from types import MethodType

st = Student('dwj', 12)
print(st.name + ', ' + str(st.age))


def set_score(self,score):
    if not isinstance(score,int):
        raise ValueError('score must be an interge')
    if score < 0 or score > 100:
        raise ValueError('score must be in range')
    self.score = score

st.set_score = MethodType(set_score,st)
st.set_score(12)
print(str(st.score))

st.addr = "jiangsu"

print(st.addr)

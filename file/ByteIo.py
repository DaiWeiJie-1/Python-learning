from io import BytesIO

def printByte(str):
    f = BytesIO()
    f.write(str.encode('utf-8'))
    print(f.getvalue())

printByte("hello world")



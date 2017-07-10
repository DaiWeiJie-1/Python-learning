from io import StringIO

def strIo(str):
    f = StringIO()
    f.write("Helloword\n")
    f.write("str")
    print(f.getvalue())

strIo("dwj")

def readStrIoByline(str):
    f = StringIO(str)
    while True:
        s = f.readline()
        if s == '':
            print("end")
            break
        print(s.strip())

    
readStrIoByline("hello!\n Hi\nGoodby\n")
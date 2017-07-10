
import os

def readFile():
    #取路径需要完整路径, 注意\转义;   'r'表示只读
    f = open('H:\\project\\My-Code\\Python-learning\\file\\.vscode\\launch.json','r')
    content = f.read()
    print(content)
    # 文件使用完成后必须要关闭,防止占用资源
    f.close()



def safeReadFile():
    try:
        f = open('/no/file','r')
    finally:
        if f:
            f.close()

def simpleSafeReadFile():
    # with 会处理try/catch异常并在代码块结束的时候关闭file，使用简洁
    with open('no/file','r') as f:
        # 一次性读取文件全部内容,可能会引起内存爆炸
        print(f.read())

        # 一次性读取全部内容并按行产生list
        for line in f.readlines():
            print(line)
        # 一次读一行
        f.readline()

        #读取固定长度内容
        f.read(size)

def writeFile():
    f = open("H:\\project\\My-Code\\Python-learning\\file\\.vscode\\test-writeFile",'w')
    f.write("Hello world\n")
    f.writelines("Hi dwj")
    f.close
    
def safeWriteFile():
    # with ... as .. 会安全的控制读写文件,如果文件关闭的时候没有调用close,本来可能没有写入的内存会丢失
    # with ... as .. 能够保证写入
    with open("H:\\project\\My-Code\\Python-learning\\file\\.vscode\\test-writeFile","w") as f:
        f.write("hello world!")



def listDir(path):
    # 由于isDir判断的是绝对路径,所以需要用join将path和文件名拼起来判断
    d = [x for x in os.listdir(path) if os.path.isdir(os.path.join(path,x))]
    for fileName in d:
        print(fileName)






# readFile()

# writeFile()

listDir("H:\\project\\My-Code\\Python-learning")
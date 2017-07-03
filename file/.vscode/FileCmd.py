

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
    with open('no/file','r') as f:
        print(f.read)

readFile()


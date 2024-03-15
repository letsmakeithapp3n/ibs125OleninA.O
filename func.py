#1
def upper(t:str)->str:
    x=""
    for i in t:
        if i.isupper():
            x+=i
    print(x)
#2
def punct(u:str)->str:
    tcunup = ['!', '?','.',',', '(', ')']
    count = 0
    for i in tcunup:
        if i in u:
            count+=1
    print(count)
#3
def createCube(a: int,b:int):
    for i in range(a):
        print('*'*b)
#4
def double(x:str)->str:
    y=""
    for i in x:
        y+=i*2
    print(y)
#6
def strangeList(x: int,y = 0):
    arr = []
    while len(arr) < x:
        arr.append(y)
    print(arr)
#5
def setsCount(detCnt:int, figCnt:int, carCnt:int, treeCnt:int):
    minDet=min(detCnt // 72, figCnt // 4, carCnt // 2, treeCnt // 7)
    print(minDet)
#7
def customFilter(x:list):
    sum = 0
    for i in x:
        if isinstance(i,int):
            if i % 7 == 0:
                sum += i
    print(sum > 83)
def plainJane(x:int,y:int):
    print("_"*y)
    for i in range(x):
        a = 1
        for j in range(y):
            print(f"|{a}|", end=" ")
            a += 1
        print()
    print("-"*y)

strangeList(4,8)
upper("HeLlAwW")
punct('str()?')
createCube(2,4)
double('str')
setsCount(72,4,2,7)
customFilter([1,89,"text",77])
plainJane(4,3)

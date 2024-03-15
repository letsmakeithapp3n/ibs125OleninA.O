all_keys = ['red key', 'blue key', 'golden key', 'red key', 'blue key', 'white key', 'golden key']
x = 0
for i in all_keys:
    if i == ("golden key"):
        x = x + 1
print("True")
print(x)


while True:
    print("a= ")
    a = int(input())
    print("b = ")
    b = int(input())
    if a <= 0 or b <= 0:
        print("try again")
    else:
        print(a * b)
        break


msg = '6_185+_7*/#4i/*(@n'
for i in msg:
    if i=='7':
        i='п'
    elif i=='1':
        i='т'
    elif i=='n':
        i='!'
    elif i== '+':
        i='я'
    elif i=='i':
        i='и'
    elif i=='/':
        i='л'
    elif i=='(':
        i='с'
    elif i=='5':
         i='б'
    elif i=='6':
         i='у'
    elif i=='_':
         i=' '
    elif i=='*':
         i='о'
    elif i=='8':
         i='e'
    elif i=='#':
         i='у'
    elif i== '4':
         i='ч'
    else:
         i='ь'
    print(i,end='')


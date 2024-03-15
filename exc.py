while True:
    a=0
    try:
        x = int(input("Введите целое положительное число"))
        if x >= 0:
            while a <= x:
                print(a, end=" ")
                a += 1
            break
        else:
            print("Число должно быть больше нуля")
    except ValueError:
        print("вы ввели не число")

arr = [1,2,3,4,5,6]
for i,j in enumerate(arr):
    try:
            print(j / i)
    except ZeroDivisionError:
        print(f"Деление на 0! Элемент {j} ")

arr1 = []
for i in range(5):
    while len(arr1) < 5:
        try:
            arr1.append(int(input()))
        except ValueError:
            print("wrong value")
print(arr1)

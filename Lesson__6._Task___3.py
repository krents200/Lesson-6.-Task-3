print ('Введите 2 целых числа через пробел:')
a, b = map(int, input().split())
c = 0
if a > b:
    c = a
    a = b
    b = c
print ('Чётные числа на отрезке:')
for i in range(a, b+1): #Отрезок подразумевает включённые точки
    if i % 2 == 0:
        print (i)

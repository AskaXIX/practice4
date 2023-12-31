# В фермерском хозяйстве в Карелии выращивают чернику. Она растёт на круглой грядке, причём кусты высажены только по окружности. Таким образом, у каждого куста есть ровно два соседних. 
# Всего на грядке растёт N кустов. Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод — на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники. Эта система состоит из управляющего модуля и нескольких собирающих модулей. 
# Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль, находясь перед некоторым кустом заданной во входном файле грядки.

# n = int(input())
# a = list(map(int, input().split()))
# x = 0
# i = 1
# for i in range (n):
#     if (a[i]+a[i+1]+a[i-1] > x):
#         x = a[i]+a[i+1]+a[i-1]
# print(x)

n = int(input('n = '))

lst = [int(x) for x in input().split()]

n = len(lst)

lst = lst + lst[:2]

m = 0
for i in range(n):
    m = max(m, lst[i] + lst[i+1] + lst[i+2])
print(m)
# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

N = int (input ("Vvedite chislo: "))
sum = 0
while N != 0:
    num = N %10
    sum +=num
    N = N // 10
print(sum) 



#Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

from math import factorial

n = int(input("Vvedite chislo: "))
f = lambda x: ((x == 1) and 1) or x * factorial(x -1)
list2 = list( f(i) for i in range(1, n +1))
print(list2)



# Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.

n = int(input("Vvedite N: "))
list = [round((1+1/i)**i, 3) for i in range(1, n+1)]
print(f"Posledovatel'nost': {list}\nSumma: {round(sum(list), 3)}")


# Реализуйте алгоритм перемешивания списка.


import random
arr = [1, 2, 5, 11, 15, 21, 5, 10]
b = arr[:]
random.shuffle(b)
print(arr)
print(b)

# Условная конструкция. Операторы if, elif, else
first = int(input("Ведите целое число:"))
second = int(input("Еще одно:"))
third = int(input("Ведите последнее целое число:"))
if first == second and second == third:
    print("Вы ввели 3 одинаковых числа")
elif first == second or second == third or first == third:
    print("Вы ввели 2 одинаковых числа")
else:
    print("Число совпадений Ваших чисел равно 0")

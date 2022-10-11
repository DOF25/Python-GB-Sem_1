from email.errors import StartBoundaryNotFoundDefect
from random import randint
# #Task 1
# n = int(input("Введите день недели:"))
# if 5 < n < 8:
#     print("Да")
# else:
#     print("Нет")

# #Task 2
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             print(not (x or y or z) == (not x and not y and not z))
#             print(x, y, z)
                
# #Task 3
# def plane_number(x, y):
#     if x > 0:
#         if y > 0:
#             print("Первая плоскость")
#         else:
#             print("Четвертая плоскость")
#     if x < 0:
#         if y > 0:
#             print("Вторая плоскость")
#         else:
#             print("Третья плоскость")
# s = plane_number(int(input("Введите координаты x:")), int(input("Введите координаты y:")))
# print(s)

# #Task 4
# def calculate(x, y, operation):
#     if operation == "*":
#         return x * y
#     elif operation == "-":
#         return x - y
#     elif operation == "/":
#         if y == 0:
#             print("Деление на ноль!")
#             return
#         else:
#             return x / y
#     elif operation == "+":
#         return x + y
#     elif operation == "mod":
#         if y == 0:
#             print("Деление на ноль!")
#             return 
#         else:
#             return x % y
#     elif operation == "pow":
#         return pow(x, y)
#     elif operation == "div":
#         return x // y
# for _ in range(2):
#     x, y= (int(k) for k in input("Введите x и y: ").split())
#     oper = input("Введите операцию: ")
#     print(calculate(x, y, oper))

def mass(rows, columns):
    mas = []
    for _ in range(rows):
        a = []
        for _ in range(columns):
            a.append(randint(1, 1000))
        mas.append(a)
    print(*mas, sep="\n")
    print("---------------------")
    sorted_list = []
    for row in mas:
        sorted_list.extend(row)
    sorted_list.sort()
    print("отсортированный лист ", sorted_list)
    print("---------------------")
    mas.clear()
    for i in range(rows):
        a = sorted_list[0:columns]
        mas.append(a)
        sorted_list = sorted_list[columns:]
    print(*mas, sep="\n")

rows, columns = int(input("Количество строк: ")), int(input("Количество столбцов: "))
print(mass(rows, columns))
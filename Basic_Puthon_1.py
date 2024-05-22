# 1 Привести к целому типу - 1.6, 2.99
a = 1.6
b = 2.99
print(int(a), int(b))
# 2 Заменить символ “#” на символ “/” в строке 'www.my_site.com#about'
line = 'www.my_site.com#about'
line = line.replace('#', '/')
print(line)
# 3 Напишите программу, которая добавляет ‘ing’ к слову ‘stroka’
word = 'stroka'
print(word + 'ing')
# 4 В строке “Ivanou Ivan” поменяйте местами слова => "Ivan Ivanou"
fio = 'Ivanou Ivan'
fio = fio.replace('Ivanou Ivan', 'Ivan Ivanou')
print(fio)
# 5 Напишите программу которая удаляет пробел в начале, в конце строки
space = ' asd '
print(space.strip())
# 6 Создайте словарь, связав его с переменной school, и наполните его данными которые бы отражали количество учащихся
# в десяти разных классах (например, 1а, 1б, 2б, 6а, 7в и т.д.).
school = {
    "1a": 20,
    "1b": 22,
    "2a": 21,
    "2b": 19,
    "3a": 26,
    "3b": 24,
    "4a": 21,
    "4b": 15,
    "5a": 25,
    "5b": 29,
}
# 7 Создайте список и извлеките из него списка второй элемент.
list_el = ["anton", 24, True]

print(list_el[1])
# 8 Вывести входит ли строка1 в строку2 (пример: employ и employment )
n = 'employ'
m = 'employment'
if n in m:
    print(True)
else:
    print(False)
# 9 Вывести нужные символы
x = "My name is Agent Smith"
print(x[1]) #y
print(x[3:16:3]) #nesgt

# 10 Есть массив чисел. Известно, что каждое число в этом массиве имеет пару, кроме одного: [1, 5, 2, 9, 2, 9, 1]
# Напишите программу, которая будет выводить уникальное число => 5
arr = [1, 5, 2, 9, 2, 9, 1]
arr2 = []

for i in arr:
    if arr.count(i) == 1:
        arr2.append(i)
print(arr2)



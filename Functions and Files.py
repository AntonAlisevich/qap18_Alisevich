# 1 Дан файл целых чисел, содержащий не менее четырех элементов.
# Вывести первый, второй, предпоследний и последний элементы данного
# файла. Если чисел меньше 3 выводить ошибку

f = open('numbers', 'r')

a = f.read().split()
counter = 0

for i in a:
    counter += 1
if counter > 3:
    print(a[0])
    print(a[1])
    print(a[-1])
    print(a[-2])
else:
    print("Error")

# 2 Дан файл целых чисел. Создать два новых файла, первый из которых
# содержит четные числа из исходного файла, а второй — нечетные (в том
# же порядке). Если четные или нечетные числа в исходном файле
# отсутствуют, то соответствующий результирующий файл оставить
# пустым.

f1 = open('numbers', 'r')
b = f1.read().split()
my_file1 = open("newFile.txt", "w+")
my_file2 = open("newFile2.txt", "w+")
for i in b:
    if int(i) % 2 == 0:
        my_file1.write(i)
    elif int(i) % 2 > 0:
        my_file2.write(i)


# 3 Дан файл вещественных чисел. Заменить в нем все элементы на их
# квадраты.

f2 = open("new_numbers.py", "r")
v = f2.read().split()

v2 = [float(i) ** 2 for i in v]

f2.close()
f2 = open("new_numbers.py", "w")

for i in v2:
    f2.write(str(i) + " ")

f2.close()


# 4 Даны два файла произвольного типа. Поменять местами их
# содержимое. Файлы должны быть бинарного типа
# - Все делать с помощью функций

def bin_files(file1, file2):

        with open(file1, 'rb') as file1:
            data1 = file1.read()
        with open(file2, 'rb') as file2:
            data2 = file2.read()
        with open('file1.bin', 'wb') as file1:
            file1.write(data2)
        with open('file2.bin', 'wb') as file2:
            file2.write(data1)


bin_files('file1.bin', 'file2.bin')

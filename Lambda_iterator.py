# 1 Создать lambda функцию, которая принимает на вход имя и выводит его в формате “Hello, {name}”

greeting = lambda x: f"Hello, {x}"

print(greeting("Anton"))

# 2 Создать lambda функцию, которая принимает на вход список имен и выводит их в формате “Hello, {name}” в другой список

all = lambda names: list(map(lambda x: greeting(x), names))
names_list = ["Anton", "Sergei", "Edd"]
greetings = all(names_list)
print(greetings)

# 1 Напишите генератор который принимает список
# numbers = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7] и возвращает новый список только с положительными числами

def new_gen(numbers):
    new_numbers = [number for number in numbers if number >= 0]
    for number1 in new_numbers:
        yield number1


my_numbers = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]
my_generator = new_gen(my_numbers)

new_list =[]
for number in my_generator:
    new_list.append(number)
print(new_list)

# 2 Необходимо составить список чисел которые указывают на длину слов в строке: sentence = " thequick brown fox
# jumps over the lazy dog", но только если слово не "the" с обработкой исключений

def getting_length_of_words(sentence):
    try:
        words = sentence.split()
        lenths = [len(words) for words in words if words.upper() != 'THE']
        return lenths
    except Exception as e:
        return print(e)


my_sentence = "the quick brown fox jumps over the lazy dog"
my_words = getting_length_of_words(my_sentence)
print(my_words)



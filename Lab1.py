#Tusk1
# Створюємо змінні
zminna1 = input("Введіть перше число: ")
zminna2 = input("Введіть друге число: ")
zminna3 = input("Введіть третє число: ")
zminna4 = input("Введіть четверте число: ")

# Виводимо значення змінних
print("Значення змінних:")
print("Змінна 1:", zminna1)
print("Змінна 2:", zminna2)
print("Змінна 3:", zminna3)
print("Змінна 4:", zminna4)
#Tusk2
x = 10
y = 3

# Виконуємо арифметичні операції
suma = x + y
vidnimannya = x - y
mnozhennya = x * y
dilennya = x / y
pidnesennya_do_stepenya = x ** y
tsilochyselne_dilennya = x // y
ostacha_vid_dilennya = x % y

# Записуємо результати в список
results = [suma, vidnimannya, mnozhennya, dilennya,
pidnesennya_do_stepenya, tsilochyselne_dilennya, ostacha_vid_dilennya]

# Виводимо список результатів
print("Результати арифметичних операцій:")
for i, result in enumerate(results):
    print(f"Операція {i+1}: {result}")
#Tusk3
print("Кількість елементів у списку:", len(results))
print("Парні елементи списку:")
for element in results:
    if element % 2 == 0:
        print(element)
#Tusk4
# Поміняємо місцями другий і п’ятий елементи
results[1], results[4] = results[4], results[1]

print("Список після обміну елементів:")
print(results)
#Tusk5
name = input("Введіть ваше прізвище та ім'я: ")

print("Виконавець лабораторної роботи:", name)

# 3. Напишите и запустите блок кода, посмотрите на результат выполнения программы
x = 38

print("дратути!")
if x < 0:
    print("Меньше нуля")
print("дотвидание")

# 4. Напишите и запустите блок кода, посмотрите на результат выполнения программы
# пример
a, b = 10,  5

if a > b:
    print("a > b")

if a > b and a > 0:
    print("успех")


if (a > b) and (a > 0 or  b < 1000):
    print("успех")

if 5 < b and b < 10:
    print("успех")

# 6. Напишите и запустите блок кода, посмотрите на результат выполнения программы
# можно сравнить - числа, строки, списки, вообще-

if "34" > "123":
    print("успех")

if "123" > "12":
    print("успех")

if [1, 2] > [1, 1]:
    print("успех")

# 7. Напишите и запустите блок кода, посмотрите на результат выполнения программы
# что нельзя сравнивать разные типы
if "6" > 5:
    print("успех")

if [5, 6] > 5:
    print("успех")

# но
if "6" != 5:
    print("успех")
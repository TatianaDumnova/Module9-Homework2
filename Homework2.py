
# Задача 1: Фабрика Функций
# Написать функцию, которая возвращает различные математические функции
# (например, деление, умножение) в зависимости от переданных аргументов.
print('Задача №1: Фабрика функций')
def create_operation(operation):
    if operation == "division":
        def division(x, y): #Функция возвращает результат деления
            return x / y
        return division
    elif operation == "multiplication":
        def multiplication(x, y): #Функция возвращает результат умножения
            return x * y
        return multiplication

my_func = create_operation("multiplication")
print(my_func(3,2))
my_func = create_operation("division")
print(my_func(12,6))


# Задача 2: Лямбда-Функции
# Использовать лямбда-функцию для реализации простой операции и
# написать такую же функцию с использованием def. Например, возведение числа в квадрат
print('Задача №2: Лямбда')

multiply = lambda x: x ** 2
print(multiply(4)) # Выводит 16

def multiply_def(x):
   return x ** 2
print(multiply_def(4)) # Выводит 16


# Задача 3: Вызываемые Объекты
# Создать класс с Rect c полями a, b которые задаются
# в __init__ и методом __call__, который возвращает площадь прямоугольника, то есть a*b.
print('Задача №3: Вызываемые объекты')

class Rect:
   def __init__(self, a, b):
       self.a = a
       self.b = b
   def __call__(self):
      return self.a * self.b

area_rectangle = Rect(2,4)
print(f'Площадь: {area_rectangle()}')
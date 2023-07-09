import math

message = ('Добро пожаловать в самую лучшую программу для вычисления '
           'квадратного корня из заданного числа')


def CalculateSquareRoot(Number):
    """Вычисляет квадратный корень."""
    return math.sqrt(Number)


def calc(your_number):
    """Smth 2."""
    if your_number <= 0:
        print('Квадратного корня нет')
    else:
        root = CalculateSquareRoot(your_number)
        print('Мы вычислили квадратный корень из введённого вами числа. '
              f'Это будет: {root}')


print(message)
calc(25.5)

numerator = ''
denominator = ''

def check(numerator):
    while True:
        numerator = input("Введите число: ")
        if not numerator.isdigit():
            print("Введены не корректные данные")
            continue
        else:
            numerator = int(numerator)
            break
    return numerator
a = check(numerator)
b = check(denominator)
print(a, b)

def process(a, b):
    try:
        c = (a / b)
        print('result:', c)
    except ZeroDivisionError:
        print("Мы тут на 0 не делим")

process(a, b)


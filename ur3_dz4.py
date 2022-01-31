x = 2
y = -3

def my_func(x, y):
    c = x ** y
    print(round(c, 3))

my_func(x, y)

def my_func2(x, y):
    y = abs(y)
    for i in range(y - 1):
        x += x
    x = 1 / x
    print(x)


my_func2(x, y)

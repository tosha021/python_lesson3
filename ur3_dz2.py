A = ['Имя', 'Фамилию', 'Дату рождения', 'Город', 'Почту', 'Номер телефона']
fname, lname, bd, city, email, tn = ['']*6
a = [fname, lname, bd, city, email, tn]

for i in range(len(A)):
    print(f"Введите {A[i].lower()}:")
    a[i] = input()
    print()

def user(fname = '', lname = '', bd = '', city = '', email = '', tn = ''):
    print(fname, lname, bd, city, email, tn)

user(bd = a[2], fname = a[0], lname = a[1], city = a[3], email = a[4], tn = a[5])
def my_func():
    s_symb = 'z'
    raw_d = ''
    user_in = None
    count = 0
    switch = 0
    print("Специальный символ: 'z'")
    print("Введите строку чисел, разделенную пробелом: ")
    while user_in != s_symb:
        user_in = input()
        raw_d = user_in + ' '
        for i in range(len(raw_d)):
            if raw_d[i] != " " and raw_d[i] != s_symb:
                count += int(raw_d[i])
            elif raw_d[i] == s_symb:
                switch = 1
        print(count)
        if switch != 0:
            user_in = s_symb


my_func()

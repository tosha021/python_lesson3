a, b, c = 1, 2, 3

def my_func(a, b, c):
    A = [a,b,c]
    x = A[0]
    for i in range(len(A)):
        if x >= A[i]:
            x = A[i]
    A.remove(x)
    print(A[0] + A[1])

my_func(7, 9, 8)
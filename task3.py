n = int(input())

if (n >= 10 and n <= 20) or n % 10 ==5:
    print(n, 'лет')
elif n % 10 == 1:
    print(n, 'год')
elif n % 10 > 1 and n % 10 < 5:
    print(n, 'года')
elif n % 10 > 5 or n % 10 == 0:
    print(n, 'лет')
a1 = int(input())
b1 = int(input())
a2 = int(input())
b2 = int(input())
if b1 < a2 or b2 < a1:
    print('Пустое множество')
elif b1 == a2:
    print(a2)
elif a1 == b2:
    print(a1)
else:
    print(f'[{max(a1, a2)}; {min(b1, b2)}]')

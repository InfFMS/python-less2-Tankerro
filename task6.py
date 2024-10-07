for i in range(100, 999):
    if i == (i%10)**3 + ((i%100)//10)**3 + (i//100)**3:
        print(i)
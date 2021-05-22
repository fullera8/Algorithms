def factor(x):
    if x == 1:
        return 1
    else:
        return x * factor(x - 1)

print(f'factorial 5 = {factor(5)}, factorial 3 = {factor(3)}')
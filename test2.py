
def func(a, b=10, c=2):
    c += a + b
    return c

result = func(2, 5) + func(10) #+ func(2, 5)
print(result)
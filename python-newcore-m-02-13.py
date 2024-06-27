

def factorial(n):
    if n < 2:
        return 1
    else:
        return n * factorial(n - 1)


def number_of_groups(n, k):
    if k > n:
        return 0  # Якщо k більше за n, то сполучень бути не може
    return factorial(n) // (factorial(n - k) * factorial(k))

    
    
    
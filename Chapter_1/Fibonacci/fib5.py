def fib5(n: int) -> int:
    if n == 0: return n  # special case
    last: int = 0  # initially set to fib(0)
    next: int = 1  # initially set to fib(1)
    for _ in range(1, n):
        last, next = next, last + next
    return next


##without tuples and type hints

def fib5a(n):
    if n == 0: return n  # special case
    last  = 0  # initially set to fib(0)
    next = 1  # initially set to fib(1)
    for _ in range(1, n):
        last = next
        next = last + next
    return next

if __name__ == "__main__":
    print(fib5a(5))
    print(fib5a(50))
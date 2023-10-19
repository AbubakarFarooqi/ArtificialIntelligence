# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.

n = int(input('How Many Terms'))
memoization = [-1]*(n+1)


def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if (memoization[n] != -1):
        return memoization[n]
    memoization[n] = (fib(n-1) + fib(n-2))
    return memoization[n]


memoization[0] = (0)
memoization[1] = (1)
for i in range(n):
    print(fib(i))

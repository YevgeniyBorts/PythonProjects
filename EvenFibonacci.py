cache = {}
def fib(n):
    if n not in cache.keys():
        cache[n] = _fib(n)
    return cache[n]

def _fib(n):
    if n < 2:
        return n
    else:
        return fib(n-1) + fib(n-2)

x = []
for i in range(100):
    f = fib(i)
    if f > 4000000:
        break
    x.append(f)

y = []

for t in x:
    if t % 2 == 0:
      y.append(t)

print(y)

print(sum(y))
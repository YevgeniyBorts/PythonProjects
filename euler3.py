x = 600851475143
y = x
z = 0

count = 2

while (count * count) <= y:
    if (y % count == 0):
        y = y / count
        z = count
    else:
        count += 1

if y > z:
    z = y

print(y)
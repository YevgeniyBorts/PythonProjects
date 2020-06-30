values = [[10000, 500], [9000, 600], [5000, 1000], [3000, 1200], [0, 1500]]
i = float(input("Enter an interest rate "))


def prv(ar, r, n):
return ar * ((1-(1+r)**-n)/r)


def pv(fv, r, n):
return fv / ((1+r) ** n)


def start(values, r):
output = []
num = 0
while num < len(values):
output.append(prv(values[num][1], r, 10) + pv(values[num][0], r, 10))
print("The total present value for future value of", values[num][0], "and annual revenue of ",
values[num][1], "for 10 years at", str(i*100) + "%", "interest is $", output[num])
num += 1


while i <= 0:
i = float(input("Please enter a valid interest rate: "))
else:
start(values, i)
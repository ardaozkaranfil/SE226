#q1
def factorial(x):
    if x == 0 or x == 1:
        return 1
    return x * factorial(x - 1)

#q2
abs_val = lambda x, i: (x ** (2 * i)) / factorial(2 * i)

def exp_x(x, n):
    result = 0
    for i in range(n):
        result += ((-1) ** i) * abs_val(x, i)
    return result

#q3
Gn = 0

def geometric_series(n, r):
    global Gn
    if n < 0:
        return

    Gn += r**n
    geometric_series(n - 1, r)

#main
if(__name__) == "__main__":
    print("Q1:")
    val = int(input("Enter a number: "))
    print(f"{val}! = {factorial(val)}")

    print("Q2:")
    x = float(input("Enter x: "))
    n = int(input("Enter n: "))
    print(f"S = {exp_x(x, n)}")

    print("Q3:")
    nq3 = int(input("Enter n: "))
    r = float(input("Enter r: "))
    Gn = 0
    geometric_series(nq3, r)
    print(f"Gn = {Gn}")

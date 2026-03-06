n = int(input("Please enter a positive integer greater than 9:"))
steps = 0
sum = 0
while n > 9:

    if n > 10:
        print(n , "→",end=" ")
    elif n == 10:
        print("10", "→", "1")
        steps+=1
        break
    else:
        print(n)
        break

    steps += 1

    while n > 0:
        temp = n
        temp %= 10
        sum += temp
        n //= 10

    n = sum
    sum = 0

print(n)
print("Final Value:", n)
print("Total Steps:", steps)
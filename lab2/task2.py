n = int(input("Please enter a number between 10 and 100:"))
while n < 10 or n > 100:
    n = int(input("Invalid input. Please enter a number between 10 and 100:"))
fizzCount = 0
buzzCount = 0
fizzbuzzCount = 0

for i in range(1, n + 1):
    if i % 7 == 0:
        continue
    elif i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
        fizzbuzzCount += 1
    elif i % 3 == 0:
        print("Fizz")
        fizzCount += 1
    elif i % 5 == 0:
        print("Buzz")
        buzzCount += 1
    else:
        print(i)
print("--- Summary ---")
print("Fizz count: ", fizzCount)
print("Buzz count: ", buzzCount)
print("FizzBuzz count: ", fizzbuzzCount)
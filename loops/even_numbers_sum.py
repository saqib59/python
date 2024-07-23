n = 10
sum_even = 0

for item in range(1, n+1):
    if item % 2 == 0:
        sum_even += 1

print(f"sum of even numbers {sum_even}")
number = 2
table = 10

for item in range(1, table+1):
    if (item == 5):
        continue

    print(f"{number} x {item} = {item * number}")
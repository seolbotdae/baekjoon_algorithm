n = int(input())

number = 666
count = 1

while True:
    if count >= n:
        break

    number += 1

    if str(number).count("666") > 0:
        count += 1

print(number)
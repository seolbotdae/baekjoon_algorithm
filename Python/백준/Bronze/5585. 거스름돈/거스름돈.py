money = 1000 - int(input())

count = 0

arr = [500, 100, 50, 10, 5, 1]

for item in arr:
    count += money // item
    money = money % item

print(count)
arr = []

while True:
    temp = input()
    if temp == "0":
        break

    arr.append(temp)

for item in arr:
    # 홀수개
    if len(item) % 2 == 1:
        half = len(item) // 2 

        if item[0 : half] == item[len(item) : half : -1]:
            print('yes')
        else:
            print('no')
    else:
        half = len(item) // 2 

        if item[0 : half] == item[len(item) : half - 1 : -1]:
            print('yes')
        else:
            print('no')
        
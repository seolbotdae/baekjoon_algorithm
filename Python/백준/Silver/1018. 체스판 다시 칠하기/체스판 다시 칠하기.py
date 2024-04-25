row, col = map(int, input().split())

arr = []

# 1 == "W". -1 == "B"
for i in range(row):
    temp = []

    for i in input():
        if i == "W":
            temp.append(1)
        else:
            temp.append(-1)

    arr.append(temp)

minCount = 9999999

# x, y 값을 받고 몇 개를 수정해야 하는지 알려줌
def checker(x, y):
    # 시작 지점이 무슨 블럭인지 알아냄 둘 다 돌려봐야 하기 때문
    if arr[y][x] == 1:
        # 시작 지점이 W 이라면
        startAt = 1
        otherStartAt = -1

    else:
        # 시작 지점이 B라면
        startAt = -1
        otherStartAt = 1

        
    count = 0
    cur = startAt

    for ver in range(y, y+8):
        for hor in range(x, x + 8):
            if arr[ver][hor] != cur:
                count += 1
            
            if hor != x + 7:
                cur *= -1

    otherCount = 0
    cur = otherStartAt

    for ver in range(y, y+8):
        for hor in range(x, x + 8):
            if arr[ver][hor] != cur:
                otherCount += 1
            
            if hor != x + 7:
                cur *= -1
    
    if otherCount < count:
        return otherCount
    else:
        return count

for vertical in range(row - 7):
    for horizontal in range(col - 7):
        result = checker(horizontal, vertical)
        
        if minCount > result:
            minCount = result

print(minCount)

input()
L = list(map(int, input().split()))
L.sort()
max = L[-1]
average = 0
for i in range(len(L)):
    L[i] = L[i]/max * 100
    average+=L[i]

print(average/len(L))
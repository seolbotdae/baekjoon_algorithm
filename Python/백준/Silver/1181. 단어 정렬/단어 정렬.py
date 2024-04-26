n = int(input())

wordsSet = set()

for _ in range(n):
    word = input()
    wordsSet.add((len(word), word))
    
# 튜플을 정렬할 경우, 앞의 원소를 기준으로 정렬하고, 앞의 원소끼리 같을 경우 뒤의 원소를 기준으로 정렬
result = sorted(wordsSet)

for i, word in result:
    print(word)
n = int(input())

wordsSet = set()

for _ in range(n):
    word = input()
    wordsSet.add((len(word), word))
    

result = sorted(wordsSet)

for i, word in result:
    print(word)
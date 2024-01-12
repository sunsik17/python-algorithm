n = int(input())
result = [-1 for _ in range(11)]
answer = 0
for _ in range(n):
    cow, index = map(int, input().split())

    if result[cow] == -1:
        result[cow] = index
        continue

    if result[cow] != index:
        answer += 1
        result[cow] = index


print(answer)
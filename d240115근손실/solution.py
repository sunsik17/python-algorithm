N, K = map(int, input().split())

kits = [int(num) for num in input().split(" ")]
visited = [False] * N
count = 0
result = 0


def dfs(weight):
    global count, result
    if weight < 500:
        return
    if count == N:
        result += 1
        return

    for i in range(N):
        if not visited[i]:
            visited[i] = True
            weight = weight - K + kits[i]
            count += 1
            dfs(weight)
            visited[i] = False
            weight = weight + K - kits[i]
            count -= 1


dfs(500)
print(result)

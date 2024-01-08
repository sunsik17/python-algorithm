arr = []
nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

def solution(N):
  
  if N > 1023:
    return -1
  
  __dfs(0, 0)
  arr.sort()
  return arr[N - 1]
  

def __dfs(sum, idx):
  if sum not in arr:
    arr.append(sum)

  if idx > 9:
    return

  __dfs(sum * 10 + nums[idx], idx + 1)
  __dfs(sum, idx + 1)
  

N = int(input())
print(solution(N))
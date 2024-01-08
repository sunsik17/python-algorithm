import math
N, L, W, H = map(int, input().split())

start = 0
end = 1_000_000_000
count = 0
while count < 100:
  mid = (start + end) / 2
  if (L // mid) * (W // mid) * (H // mid) >= N:
    start = mid
  else:
    end = mid
  count += 1

print(f'{end: .10f}')



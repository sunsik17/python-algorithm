import math
N, L, W, H = map(int, input().split())

start = 0
end = 1_000_000_000

for i in range(100):
  mid = (start + end) / 2
  if (L // mid) * (W // mid) * (H // mid) >= N:
    start = mid
  else:
    end = mid

print(f'{end: .15f}')



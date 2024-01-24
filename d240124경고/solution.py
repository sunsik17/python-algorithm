h, m, s = map(int, input().split(':'))
h2, m2, s2 = map(int, input().split(':'))

res_h, res_m, res_s = h2 - h, m2 - m, s2 - s


if res_s < 0:
    res_s += 60
    res_m -= 1

if res_m < 0:
    res_m += 60
    res_h -= 1

if res_h < 0:
    res_h += 24

answer = f'{res_h:02d}:{res_m:02d}:{res_s:02d}'
print(answer if answer != '00:00:00' else '24:00:00')
bomb = dict()

bomb['***\n* *\n* *\n* *\n***'] = '0'
bomb['  *\n  *\n  *\n  *\n  *'] = '1'
bomb['***\n  *\n***\n*  \n***'] = '2'
bomb['***\n  *\n***\n  *\n***'] = '3'
bomb['* *\n* *\n***\n  *\n  *'] = '4'
bomb['***\n*  \n***\n  *\n***'] = '5'
bomb['***\n*  \n***\n* *\n***'] = '6'
bomb['***\n  *\n  *\n  *\n  *'] = '7'
bomb['***\n* *\n***\n* *\n***'] = '8'
bomb['***\n* *\n***\n  *\n***'] = '9'

arr = []
for i in range(5):
    arr.append(input())

length = len(arr[0])
result = [['' for _ in range(5)] for _ in range((length + 1) // 4)]

is_valid = True
for i in range(5):
    idx = 0
    star = ''
    for j in range(length):
        if not is_valid:
            is_valid = True
            continue
        star += (arr[i])[j]
        if len(star) == 3:
            if j < length - 1:
                is_valid = False
            result[idx][i] = star
            idx += 1
            star = ''


def solution(res):
    a = ''
    for s in res:
        _str = '\n'.join(s)
        if _str not in bomb.keys():
            return 'BOOM!!'
        else:
            a += bomb[_str]

    if a.isdigit():
        if int(a) % 6 == 0:
            return 'BEER!!'
        else:
            return 'BOOM!!'


print(solution(result))

# 씨바 개같네 문제 진짜

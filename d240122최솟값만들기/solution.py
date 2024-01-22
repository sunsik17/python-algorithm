from collections import deque


def solution(A, B):
    answer = 0
    A.sort()
    B.sort()
    l = len(B) - 1
    for i in range(len(A)):
        answer = answer + (A[i] * B[l])
        l -= 1

    return answer





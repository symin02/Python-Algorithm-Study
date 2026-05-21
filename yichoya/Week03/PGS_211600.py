# 소수찾기
import sys
sys.setrecursionlimit(10**6)

def solution(numbers):
    n = len(numbers)
    visited = [False] * n
    ans = set()

    def isPrime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    def recur(tmp):
        if tmp:
            num = int(tmp)
            if isPrime(num):
                ans.add(num)

        for i in range(n):
            if not visited[i]:
                visited[i] = True
                recur(tmp + numbers[i])
                visited[i] = False

    recur("")
    return len(ans)
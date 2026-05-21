# 타겟 넘버
def solution(numbers, target):
    answer = 0

    def recur(cur, depth):
        nonlocal answer

        if depth == len(numbers):
            if cur == target:
                answer += 1
                return

        recur(cur + numbers[depth], depth + 1)
        recur(cur - numbers[depth], depth + 1)

    recur(0, 0)
    return answer
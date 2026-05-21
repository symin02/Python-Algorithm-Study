# 피로도
def solution(k, dungeons):
    n = len(dungeons)
    visited = [False] * n
    ans = -1

    def recur(cur, cnt):
        nonlocal ans

        ans = max(ans, cnt)

        for i in range(n):
            if cur >= dungeons[i][0] and not visited[i]:
                visited[i] = True
                recur(cur - dungeons[i][1], cnt + 1)
                visited[i] = False

    recur(k, 0)
    return ans
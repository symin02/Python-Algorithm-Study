from typing import List

class Solution:
    def compress(self, chars: List[str]) -> int:
        cnt = 0             # 현재 문자가 연속해서 나온 횟수
        idx = 0             # 압축 결과를 chars에 쓸 위치
        curr = chars[0]     # 현재 확인 중인 문자 그룹

        for i in range(len(chars)):
            if chars[i] == curr:
                # 같은 문자가 계속 나오면 개수 증가
                cnt += 1
            else:
                # 문자가 바뀌면 이전 문자 그룹을 chars에 저장
                chars[idx] = curr
                idx += 1

                # 개수가 2 이상이면 숫자를 한 자리씩 저장
                if cnt > 1:
                    for n in str(cnt):
                        chars[idx] = n
                        idx += 1
                    
                # 새로운 그룹 초기화
                cnt = 1
                curr = chars[i]

        # 마지막 그룹 저장
        chars[idx] = curr
        idx += 1

        if cnt > 1:
            for n in str(cnt):
                chars[idx] = n
                idx += 1

        return idx
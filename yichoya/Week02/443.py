from typing import List

class Solution:
    def compress(self, chars: List[str]) -> int:
        cur = chars[0]
        cnt = 0    # 연속 등장 횟수
        write_idx = 0    # 압축 결과를 덮어쓸 위치

        for i in range(len(chars)):
            # 같은 문자 갯수 카운트
            if chars[i] == cur:
                cnt += 1
            else:
                chars[write_idx] = cur
                write_idx += 1
                if cnt > 1:
                    for c in str(cnt):
                        chars[write_idx] = c
                        write_idx += 1

                # 새로운 문자로 cur 업데이트
                cur = chars[i]
                cnt = 1

        # 마지막 구간 기록
        chars[write_idx] = cur
        write_idx += 1
        if cnt > 1:
            for c in str(cnt):
                chars[write_idx] = c
                write_idx += 1

        del chars[write_idx:]
        return write_idx
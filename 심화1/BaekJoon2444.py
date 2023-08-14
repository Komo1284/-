"""문제
예제를 보고 규칙을 유추한 뒤에 별을 찍어 보세요.

입력
첫째 줄에 N(1 ≤ N ≤ 100)이 주어진다.

출력
첫째 줄부터 2×N-1번째 줄까지 차례대로 별을 출력한다."""

"""
n = int(input())
for i in range(2*n-1):
    if i*2+1 <= 9:
        print(("*"*(i*2+1)).center(9))
    else :
        print(("*"*(9-((i-4)*2))).center(9))

for문 하나로 통일하고 싶어서 이렇게 코드를 썻는데 왜 인지모르겠지만
백준에서는 정답으로 인정을 안해줌..;"""


n = int(input())
for i in range(1, n):
    print(' '*(n-i) + '*'*(2*i-1))
for i in range(n, 0, -1):
    print(' '*(n-i) + '*'*(2*i-1))
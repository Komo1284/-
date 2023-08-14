"""문제
알파벳 소문자로만 이루어진 단어가 주어진다. 이때, 이 단어가 팰린드롬인지 아닌지 확인하는 프로그램을 작성하시오.

팰린드롬이란 앞으로 읽을 때와 거꾸로 읽을 때 똑같은 단어를 말한다. 

level, noon은 팰린드롬이고, baekjoon, online, judge는 팰린드롬이 아니다.

입력
첫째 줄에 단어가 주어진다. 단어의 길이는 1보다 크거나 같고, 100보다 작거나 같으며, 알파벳 소문자로만 이루어져 있다.

출력
첫째 줄에 팰린드롬이면 1, 아니면 0을 출력한다."""

"""
s = input()
n = 0
front = []
back = []
if n % 2 == 0 :
    n = len(s)//2
    for i in range(len(s)):
        if i+1 <= n :
            front.append(s[i])
        elif i+1 > n :
            back.append(s[i])
else: 
    n = len(s)//2+1
    for i in range(len(s)):
        if i+1 < n :
            front.append(s[i])
        elif i+1 > n :
            back.append(s[i])

back_1 = back[::-1]
result = 0
for i in range(len(front)):
    if ord(front[i]) == ord(back_1[i]) :
        result = 1
    else : 
        result = 0
        break
print(result)

이 문제 역시 정상적으로 동작하는 코드라고 생각하는데 채점을 99퍼까지 가서는 틀렸다고 나온다..
단순히 리버스를 이용해서 풀 수 있는 문제였는데 너무 어렵게 생각해서 리스트를 반으로 쪼개서 
맞는지 일일히 대조해야 되는줄 알고 코드가 너무 길어져 버렸다.
"""

word = list(str(input()))

if list(reversed(word)) == word:
    print(1)
else:
    print(0)


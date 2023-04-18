# 백준 10950 : A+B -3
##input,split, range 활용문제

# input 문자열입력
T = int(input())  # T의 갯수만큼 input 받기
for i in range(T):  # 연속된 숫자(정수)를 생성
    # int 정수변환,map 괄호에 두개의 인자입력
    # split 공백기준으로 나누기
    a, b = map(int, input().split())
    print(a + b)  # 실행될때마다 a+b값 출력

# 9655. 돌 게임
# https://www.acmicpc.net/problem/9655

s = int(input())

if(s%2 == 0):   print("CY")
else:           print("SK")

# 숏코딩

print("CY"if int(input())%2==0 else"SK")    # 삼항연산자 사용 및 불필요한 공백과 변수 제거

print(["CY","SK"][int(input())%2])          # 튜플 + 모듈러 연산

print(["CY","SK"][int(input())&1])          # 튜플 + 비트 연산 (&1 연산을 통해 홀수 여부만 판별)

print("CSYK"[int(input())&1::2])            # 문자열 슬라이싱 + 비트 연산
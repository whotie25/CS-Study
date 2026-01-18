def isNimSumZero(lst): # return Nim-sum
    cnt = len(lst)
    res = lst[0]
    for i in range(1, cnt):
        res ^= lst[i]

    if(res == 0):
        return True
    else:
        return False
    
def isSumZero(lst): # return Sum
    cnt = len(lst)
    sum = 0
    for i in range(0, cnt):
        sum += lst[i]

    if(sum == 0):
        return True
    else:
        return False

# main
s = list(map(int, input("각 돌더미에 놓여진 돌멩이의 수를 공백으로 구분하여 입력하시오 : ").split())) # ex. 3 7 4 -> [3, 7, 4]

if(isSumZero(s)): # exception
    print("!!! 승패를 가릴 수 없습니다 !!!")
    exit()

size = len(s)

while(True):
    for i in ("선공", "후공"):
        print("\n현재 돌더미의 상황 : " + str(s))
        print("XOR 연산 결과(X) : " + ("X = 0 (당신이 불리합니다)\n" if isNimSumZero(s) else "X != 0 (당신이 유리합니다)\n"))
        tmp = list(map(int, input(i + "(선택한 돌더미 번호와 가져올 돌멩이의 수를 공백으로 구분하여 입력) : ").split()))
        # ex. 1 4 -> [1, 4] (1번 인덱스의 돌더미에서 돌멩이 4개를 가져옴) ([3, 7, 4] -> [3, 3, 4])
        
        if(len(tmp) != 2): # parameter exception
            print("!!! 잘못된 입력입니다 !!!")
            exit()

        if(tmp[0] < 0 or tmp[0] >= size): # index exception
            print("!!! 해당 번호를 갖는 돌더미가 존재하지 않습니다 !!!")
            exit()
        
        if(tmp[1] <= 0 or tmp[1] > s[tmp[0]]): # number exception
            print("!!! 돌더미의 돌멩이 수가 충분하지 않거나 가져오려는 돌멩이의 수가 0 또는 음수입니다 !!!")
        else:
            s[tmp[0]] -= tmp[1]

        if(isSumZero(s)):
            print("\n!!! " + i + "의 승 !!!") # victory
            exit()

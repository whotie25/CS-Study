# 9657. 님 게임
# https://www.acmicpc.net/problem/11694

def nimSum():
    res = 0
    for i in range(size):
        res ^= nimPiles[i] # XOR
    return res

def msb(_num):
    if _num==0: return 0 # msb(0) = 0
    tmp = 1
    while(_num >= tmp):
        tmp <<= 1
    return tmp >> 1
    
def countGreaterThanOne():
    res = 0
    for i in range(size):
        if(nimPiles[i]>1): res+=1
    return res
    
def countOne():
    res = 0
    for i in range(size):
        if(nimPiles[i]==1): res+=1
    return res
    
def deleteAnyPile():
    for i in range(size):
        if(nimPiles[i] > 0):
            nimPiles[i] = 0
            return
        
def makeNimSumZero(_s, _msb):
    for i in range(size):
        if(nimPiles[i]^_msb < nimPiles[i]):
            nimPiles[i] ^= _s
            return

def game():
    while(True):
        for i in range(2):
            onePile = countGreaterThanOne()
            if(onePile < 2):
                if(onePile == 1): return i
                return (i+1)%2 if countOne()%2 else i
            else:
                s = nimSum()
                if(s == 0): deleteAnyPile()
                else:
                    makeNimSumZero(s, msb(s))

# main
size = int(input())
nimPiles = list(map(int, input().split()))

print("cubelover" if game() else "koosaga")
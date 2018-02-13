## 모듈 : 스다하클 중 제일 큰거 반환해주는 함수 만들기

ls = ['♠','◆','♥','♣']

def joker(lss) :
    kt = []
    for i in lss :
        if i == '♠' :
            kt.append(4)  
        if i == '◆' :
            kt.append(3)
        if i == '♥' :
            kt.append(2)
        if i == '♣' :
            kt.append(1)
    s = max(kt)
    return ls[4-s]
open('/Users/프랜즈/Desktop/gui/main_window.ui','r')


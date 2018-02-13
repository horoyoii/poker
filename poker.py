import functools
import random
import tes # 족보함수 있는 모듈
from time import *

# 카드 모음집
s = ['♠'+str(i) for i in range(1, 11)] + ['♠J','♠Q','♠K']
s = ['♠'+str(i) for i in range(1, 11)] + ['♠J','♠Q','♠K']
s = ['♠'+str(i) for i in range(1, 11)] + ['♠J','♠Q','♠K']
s = ['♠'+str(i) for i in range(1, 11)] + ['♠J','♠Q','♠K']

ss = ['♣A', '♣2', '♣3', '♣4', '♣5', '♣6', '♣7', '♣8', '♣9', '♣10', '♣J', '♣Q', '♣K']

cards =[[],[],[],[]]  # 카드뭉치
for i, k in enumerate(['♠','◆','♥','♣']) :
    cards[i]=[k+'A']+[k+str(j) for j in range(2, 11)] + [k+'J',k+'Q',k+'K']

#카드덱에서 셔플로 두 개의 바구니에 하나하나씩 분배한다. 분배함을 보여주기 위해서 sleep(1.5) 설정
my_deck = [];your_deck = []
# 자본
my_money = 10000;your_money = 10000;sums = 0

# 카드분배 step.1
print('\n **7 POKER START**\n')
sleep(1)
print('기본금 : 500원')
my_money -= 500
your_money -= 500
sums += 1000
#sleep(1)
print('카드 분배')

#선 정하기 가위바위보??

# 카드묶음 섞기 / cards 의 값들을 하나로 합친 후 (deck) shuffle을 통하여 무작위 섞은 후 앞에서부터 하나씩 분배
deck = functools.reduce(lambda x,y : x+y, cards)
random.shuffle(deck)
for i, c in enumerate(deck) :
    if i == 10 :
        break
    elif i % 2 == 0 :
        your_deck.append(c)
    else :
        my_deck.append(c)
## 5장씩 배분완료!
#print(my_deck, your_deck)






#보드판 표출 함수
def board_square(my, your) :
    print('='*60)
    print('mine', end='');print('\t'*7, end='');print('yours\n')

    for i in range(len(my_deck)) :
        sleep(2)
        print(my_deck[i], end='')
        print('\t'*7+your_deck[i])

    print('='*60)
    sleep(2)


# 공개카드 한장 앞으로 내밀기
def board_square1(my, your, num, num1) :
    print('='*60)
    print('mine', end='');print('\t'*7, end='');print('yours\n')

    for i in range(len(my_deck)) :
        if i+1 == num :
            print('\t'*2+my_deck[i], end='')    
            if i+1 == num1 :
                print('\t'*2+your_deck[i])
            else :
                print('\t'*5+your_deck[i])
            continue
        elif i+1 == num1 :
            print(my_deck[i], end='')
            print('\t'*5+your_deck[i])
            continue
        print(my_deck[i], end='')
        print('\t'*7+your_deck[i])

    print('='*60)



# 보드판 표출 / 한장 비공개
board_square(my_deck, your_deck)

# 한장씩 공개함수
def open(my, your, nn):  # nn 시행차수 1: 첫번째 공개 / 2: 두번째 공개
    if nn == 1 :    
        print('\n\n**my_deck에서 공개할 한장 선택**')
        for i, v in enumerate(my) :
            if i == len(my)-1 :
                print(str(i+1)+'.'+v)
                break    
            print(str(i+1)+'.'+v, end=' / ')
        while True :
            try :
                global num
                num = int(input('선택해주세요'))
                break
            except ValueError :
                print('1~5 사이의 값을 입력해주세요.')
                continue
        
        print('\n\n**your_deck에서 공개할 한장 선택**')
        for i, v in enumerate(your) :
            if i == len(your)-1 :
                print(str(i+1)+'.'+v)
                break    
            print(str(i+1)+'.'+v, end=' / ')
        global num1
        num1 = int(input('선택해주세요'))
    elif nn == 2 :
        print('\n\n**my_deck에서 공개할 한장 선택**')
        #my_deck이 있고 [1,2,3,4,5,6] (num-1) 이 지정

        
        #my1 = my[:num-1]+my[num:]
        for i, v in enumerate(my) : # 1.♠Q / 2.♥3 / 3.◆J / 4.♥Q / 5.♥K / 6.ㅇ3
            if i == len(my)-1 :
                print(str(i+1)+'.'+v)
                break                    
            print(str(i+1)+'.'+v, end=' / ')

        while True :
            global num2
            num2 = int(input('선택해주세요'))
            if num2 == num :
                print('이미 공개된 카드입니다. 다른 것을 선택해주세요')
                continue
            break

        print('\n\n**your_deck에서 공개할 한장 선택**')
        for i, v in enumerate(your) :
            if i == len(your)-1 :
                print(str(i+1)+'.'+v)
                break    
            print(str(i+1)+'.'+v, end=' / ')

        while True :
            global num3
            num3 = int(input('선택해주세요'))
            if num3 == num1 :
                print('이미 공개된 카드입니다. 다른 것을 선택해주세요')
                continue
            break
        


    # 오픈카드 선택 후 보드팬 재출력
    
# 한장씩 공개
num = 0;num1=0   # 각 덱에서 첫번째로 공개할 카드의 인덱스
num2 = 0;num3=0   # 각 덱에서 두번째로 공개할 카드의 인덱스
open(my_deck, your_deck, 1)
board_square1(my_deck, your_deck, num, num1)


#선 정하기 / 선정하기함수 return값 : me or you / me 면  my-your 순으로
def who_is_first(num, num1) :
    me = my_deck[num-1]     #  ♣K
    you = your_deck[num1-1] #  ♠7
    # 1.숫자로 판단  2. 숫자가 같다면 문양으로 판단
    if me[1:] != you[1:] :
        lst=['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        m = lst.index(me[1:])
        y = lst.index(you[1:])
        if m > y :
            return 1
        else :
            return 2
    else :
        lstt = ['♠','◆','♥','♣']
        m = lstt.index(me[0])
        y = lstt.index(you[0])
        if m < y :
            return 1
        else :
            return 2

# 선 정하기
kk = who_is_first(num, num1)  # kk값이 1 이면 me 먼저, 2 이면 you 먼저




# 배팅 함수
def bet(kk, my_money, your_money, sums) :
    lst = ['콜','더블','하프','쿼터','체크','삥','다이']
    for i, v in enumerate(lst) :
        if i == 6 :
            print(str(i+1)+'.'+v)
            break
        print(str(i+1)+'.'+v, end = '')

    m = my_money # 9500
    y = your_money # 9500
    s = sums # 1000

    #상위 while문을 끝내려면??
    debut = True
    while debut :
        if kk == 1 :  # 나 먼저 선택
            print('** I의 배팅 **')
            choice_of_mine = int(input())
            if choice_of_mine == 1 :
                print('시작부터 call할 순 없습니다.')
                continue
            elif choice_of_mine == 5 : # 체크
                print(' I 의 체크')
                while True :
                    print('**  YOU의 배팅 **')
                    choice_of_yours = int(input()) 
                    if choice_of_yours == 1 : # 체크
                        print('체크 불가')
                        continue
                    elif choice_of_yours == 2 :
                        print('더블 불가')
                        continue
                    elif choice_of_yours == 3 : # 하프
                        print(' YOU 의 하프 ')
                        y -= s/2
                        p = s/2
                        s += s/2
                        print('** I의 배팅 ** ')
                        choice_of_mine = int(input())
                        if choice_of_mine == 1 :
                            print(' I 의 콜 ')
                            print(m)
                            m -= p
                            print(m)
                            s += p
                            debut = False
                            print('배팅 종료')
                            return m, y,s 
                            break
                    #elif choice_of_yours == 4 :
                    #elif choice_of_yours == 5 :
                    #elif choice_of_yours == 6 :
                    #elif choice_of_yours == 7 :
            elif choice_of_mine == 6 : # 삥
                print(' I 의 체크')
                print('**  YOU의 배팅 **')
                choice_of_yours = int(input())
                    #if choice_of_yours ==
            elif choice_of_mine == 7 : # 다이
                print(' I 의 체크')
                print('**  YOU의 배팅 **')
                #choice_of_yours = int(input())
        #else :          # 너 먼저 선택
                 
# 배팅
my_money, your_money, sums = bet(kk, my_money, your_money, sums)
print('\n현재 금액')
print('my money : {}'.format(my_money))
print('your_money : {}'.format(your_money))
print('배팅금액 : {}'.format(sums))

# 한장 더 배분
print()
print('!!!한장 추가!!!\n')
sleep(1)
print('='*60)
print('mine', end='');print('\t'*7, end='');print('yours\n')
for i in range(len(my_deck)) :
    if i+1 == num :
        print('\t'*2+my_deck[i], end='')    
        if i+1 == num1 :
            print('\t'*2+your_deck[i])
        else :
            print('\t'*5+your_deck[i])
            continue
    elif i+1 == num1 :
        print(my_deck[i], end='')
        print('\t'*5+your_deck[i])
        continue
    print(my_deck[i], end='')
    print('\t'*7+your_deck[i])
sleep(2)
# 누구 먼저 줄것인지 / 6장짜리 덱 완성
if kk == 1 :
    my_deck.append(deck[10])
    your_deck.append(deck[11])
else :
    your_deck.append(deck[10])
    my_deck.append(deck[11])
print(my_deck[5], end='')
print('\t'*7+your_deck[5])
sleep(1)
print('='*60)
print()
#  
# 덱에서 한장 고르는 이벤트 발생
open(my_deck, your_deck, 2)
# num2, num3 값 생성

#board_square1(my_deck, your_deck, num2, num3)
'''
sleep(1)
print('='*60)
print('mine', end='');print('\t'*7, end='');print('yours\n')
for i in range(len(my_deck)) :
    if i+1 == num :
        print('\t'*2+my_deck[i], end='')    
        if i+1 == num1 :
            print('\t'*2+your_deck[i])
        else :
            print('\t'*5+your_deck[i])
            continue
    elif i+1 == num1 :
        print(my_deck[i], end='')
        print('\t'*5+your_deck[i])
        continue
    print(my_deck[i], end='')
    print('\t'*7+your_deck[i])
sleep(2)
# 누구 먼저 줄것인지 / 6장짜리 덱 완성
if kk == 1 :
    my_deck.append(deck[10])
    your_deck.append(deck[11])
else :
    your_deck.append(deck[10])
    my_deck.append(deck[11])
print(my_deck[5], end='')
print('\t'*7+your_deck[5])
sleep(1)
print('='*60)
print()
'''
print(num, num1, num2, num3)
# 두 장 내밀기 이벤트 함수
def board_square2(my_deck, your_deck, n=0) :
    print('='*60)
    print('mine', end='');print('\t'*7, end='');print('yours\n')
    '''
    for i in range(len(my_deck)) :  # mydeck = 1.◆8 / 2.◆A / {3.◆J} / 4.♥9 / 5.♥K / 6.g3
        if i+1 == num2 :                # num / num 2   ::   num1 / num3
            print('\t'*2+my_deck[i], end='')    # num num1 < num2 num 3 경우로 생각!!
            if i+1 == num1 :
                print('\t'*2+your_deck[i])
            else :
                print('\t'*5+your_deck[i])
            continue
        elif i+1 == num3 :
            print(my_deck[i], end='')
            print('\t'*5+your_deck[i])
            continue
        print(my_deck[i], end='')
        print('\t'*7+your_deck[i])
    '''
    #for i, j in enumerate(zip(my, your)) :  # i,j = 0, (◆A, ◆J)
    #    if i == 
    for i,v in enumerate(zip(my_deck, your_deck)) :
        if i == num-1 :
            print('\t'*2+v[0], end='')
            if num-1 == num1-1 :
                print('\t'*3+v[1])
                continue
            elif num-1 == num3-1 :
                print('\t'*3+v[1])
                continue
            else :    
                print('\t'*5+v[1])
                continue
            
            
        elif i ==  num2-1 :
            print('\t'*2+v[0], end='')
            if num2-1 == num1-1 :
                print('\t'*3+v[1])
                continue
            elif num2-1 == num3-1 :
                print('\t'*3+v[1])
                continue
            else :    
                print('\t'*5+v[1])
                continue
        
        else :
            print(v[0], end='')
            if i == num1-1 :
                print('\t'*5+v[1])
                continue
            elif i == num3-1 :
                print('\t'*5+v[1])
                continue
            else :
                print('\t'*7+v[1])
                continue


    if n == 1 :
        print('='*60)

#my_deck - num ,num2
# your_deck, - num1, num3

board_square2(my_deck, your_deck, 1)

# 선 정하기

kkk = who_is_first(num2, num3)  # kkk = 1 이면 나 먼저 베팅
print(kkk)

my_money, your_money, sums = bet(kkk, my_money, your_money, sums)
print('\n현재 금액')
print('my money : {}'.format(my_money))
print('your_money : {}'.format(your_money))
print('배팅금액 : {}'.format(sums))

# my_deck 선
# 마지막 한장 분배

print()
print('!!!한장 추가!!!\n')
sleep(1)
print('='*60)
sleep(2)
board_square2(my_deck, your_deck)

# 누구 먼저 줄것인지 / 6장짜리 덱 완성
if kkk == 1 :
    my_deck.append(deck[12])
    your_deck.append(deck[13])
else :
    your_deck.append(deck[13])
    my_deck.append(deck[12])
sleep(2)
print(my_deck[6], end='')
print('\t'*7+your_deck[6])
sleep(1)
print('='*60)
print()

my_money, your_money, sums = bet(kkk, my_money, your_money, sums)
print('\n현재 금액')
print('my money : {}'.format(my_money))
print('your_money : {}'.format(your_money))
print('배팅금액 : {}'.format(sums))


print('***최종확인***')

# 족보입력
myy = tes.jock_bo(my_deck)  # 명칭, 숫자, 문양
yoo = tes.jock_bo(your_deck) # 'TP', 7 ,'t'

tree = ['RSF', 'BSF', 'SF', 'FC', 'FH', 'FL', 'MT', 'BS', 'ST', 'TR', 'TP','OP','TOP']


def changedd(a) :
    if a ==1 :
        return 'A'
    elif a == 11 :
        return 'J'
    elif a == 12 :
        return "Q"
    elif a == 13 :
        return "K"
    else :
        return a


def changed(a) :
    if a == 'RSF' :
        return '로얄 스트레이트 플레쉬'
    elif a == 'BSF' :
        return '백 스트레이트 플레쉬'
    elif a == 'SF' :
        return '스트레이트 플레쉬'
    elif a == 'FC' :
        return '포카드'
    elif a == 'FH' :
        return '풀하우스'
    elif a == 'FL':
        return '플레쉬'
    elif a == 'MT' :
        return '마운틴'
    elif a == 'BS' :
        return '백스트레이트'
    elif a == 'ST' :
        return '스트레이트'
    elif a == 'TR':
        return '트리플'
    elif a == 'TP':
        return '투페어'
    elif a == 'OP':
        return '원페어'
    else :
        return '탑'


def com(a, b) :  # a = '스페', '클로'
    db = ['♠','◆','♥','♣']
    a = 5 - db.index(a)
    b = 5 - db.index(b)
    if a > b :
        print("*** 나 승! ***")
        sleep(1)
        print("my money : {}".format(my_money+sums))
        print("your money : {}".format(your_money))
    else :
        print("*** 너 승! ***")
        sleep(1)
        print("my money : {}".format(my_money))
        print("your money : {}".format(your_money+sums))


if myy[0] != yoo[0] :
    print("\n나의 덱 : {}".format(changed(myy[0])))
    print("너의 덱 : {}\n".format(changed(yoo[0])))

    a = tree.index(myy[0])
    b = tree.index(yoo[0])

    if a < b :
        print("*** 나 승! ***")
        sleep(1)
        print("my money : {}".format(my_money+sums))
        print("your money : {}".format(your_money))
    else :
        print("*** 너 승! ***")
        sleep(1)
        print("my money : {}".format(my_money))
        print("your money : {}".format(your_money+sums))



else :
    if myy[0] == 'TOP' : # tp, 숫자, 문양 
        if myy[1] != yoo[1] :
            if tree.index(myy[1]) > tree.index(yoo[1]) :
                print("\n나의 덱 :{} {}".format(changedd(myy[1]), changed(myy[0])))
                print("너의 덱 : {} {}\n".format(changedd(yoo[1]), changed(yoo[0])))

                print("*** 나 승! ***")
                sleep(1)
                print("my money : {}".format(my_money+sums))
                print("your money : {}".format(your_money))

            elif tree.index(myy[1]) < tree.index(yoo[1]) :
                print("\n나의 덱 : {} {}".format(changedd(myy[1]),changed(myy[0])))
                print("너의 덱 : {} {}\n".format(changedd(yoo[1]),changed(yoo[0])))  

                print("*** 너 승! ***")
                sleep(1)
                print("my money : {}".format(my_money))
                print("your money : {}".format(your_money+sums))

        elif myy[1] == yoo[1] :  
            # 공통으로 쓸 문양 비교 후 결과값 표출함수만들기
            print("\n나의 덱 : {} {} {}".format(myy[2],changedd(myy[1]),changed(myy[0])))
            print("너의 덱 : {} {} {}\n".format(yoo[2],changedd(yoo[1]),changed(yoo[0])))
            com(myy[2], yoo[2])
        
    ## 여기부터 원페어로 동일 시 숫자로 비교, 숫자 동일 시 문양 비교까지~    
    elif myy[0] == 'OP' : # op, 숫자, 문양 #myy = ['op', 숫자, 문양]
        if myy[1] == 1 :
            myy[1] = 14
        if yoo[1] == 1 :
            yoo[1] = 14
        
        
        elif myy[1] > yoo[1] :
            print("\n나의 덱 :{} {}".format(changedd(myy[1]), changed(myy[0])))
            print("너의 덱 : {} {}\n".format(changedd(yoo[1]), changed(yoo[0])))

            print("*** 나 승! ***")
            sleep(1)
            print("my money : {}".format(my_money+sums))
            print("your money : {}".format(your_money))
        elif myy[1] < yoo[1] :
            print("\n나의 덱 : {} {}".format(changedd(myy[1]),changed(myy[0])))
            print("너의 덱 : {} {}\n".format(changedd(yoo[1]),changed(yoo[0])))  

            print("*** 너 승! ***")
            sleep(1)
            print("my money : {}".format(my_money))
            print("your money : {}".format(your_money+sums))   
        else :
            print("\n나의 덱 : {} {} {}".format(myy[2],changedd(myy[1]),changed(myy[0])))
            print("너의 덱 : {} {} {}\n".format(yoo[2],changedd(yoo[1]),changed(yoo[0])))
            com(myy[2], yoo[2])

    elif myy[0] == 'TP' : # myy = tp, 숫자, 문양
        if myy[1] > yoo[1] :
            print("\n나의 덱 :{} {}".format(changedd(myy[1]), changed(myy[0])))
            print("너의 덱 : {} {}\n".format(changedd(yoo[1]), changed(yoo[0])))

            print("*** 나 승! ***")
            sleep(1)
            print("my money : {}".format(my_money+sums))
            print("your money : {}".format(your_money))
        elif myy[1] < yoo[1] :
            print("\n나의 덱 : {} {}".format(changedd(myy[1]),changed(myy[0])))
            print("너의 덱 : {} {}\n".format(changedd(yoo[1]),changed(yoo[0])))  

            print("*** 너 승! ***")
            sleep(1)
            print("my money : {}".format(my_money))
            print("your money : {}".format(your_money+sums))   
        else :
            print("\n나의 덱 : {} {} {}".format(myy[2],changedd(myy[1]),changed(myy[0])))
            print("너의 덱 : {} {} {}\n".format(yoo[2],changedd(yoo[1]),changed(yoo[0])))
            com(myy[2], yoo[2])
        
    elif myy[0] == 'TR' :
        if myy[1] > yoo[1] :
            print("\n나의 덱 :{} {}".format(changedd(myy[1]), changed(myy[0])))
            print("너의 덱 : {} {}\n".format(changedd(yoo[1]), changed(yoo[0])))

            print("*** 나 승! ***")
            sleep(1)
            print("my money : {}".format(my_money+sums))
            print("your money : {}".format(your_money))
        elif myy[1] < yoo[1] :
            print("\n나의 덱 : {} {}".format(changedd(myy[1]),changed(myy[0])))
            print("너의 덱 : {} {}\n".format(changedd(yoo[1]),changed(yoo[0])))  

            print("*** 너 승! ***")
            sleep(1)
            print("my money : {}".format(my_money))
            print("your money : {}".format(your_money+sums))   
        else :
            print("\n나의 덱 : {} {} {}".format(myy[2],changedd(myy[1]),changed(myy[0])))
            print("너의 덱 : {} {} {}\n".format(yoo[2],changedd(yoo[1]),changed(yoo[0])))
            com(myy[2], yoo[2])
        
    elif myy[0] == 'ST' :
        if myy[1] > yoo[1] :
            print("\n나의 덱 :{} {}".format(changedd(myy[1]), changed(myy[0])))
            print("너의 덱 : {} {}\n".format(changedd(yoo[1]), changed(yoo[0])))

            print("*** 나 승! ***")
            sleep(1)
            print("my money : {}".format(my_money+sums))
            print("your money : {}".format(your_money))
        elif myy[1] < yoo[1] :
            print("\n나의 덱 : {} {}".format(changedd(myy[1]),changed(myy[0])))
            print("너의 덱 : {} {}\n".format(changedd(yoo[1]),changed(yoo[0])))  

            print("*** 너 승! ***")
            sleep(1)
            print("my money : {}".format(my_money))
            print("your money : {}".format(your_money+sums))
        else :
            print("\n나의 덱 : {} {} {}".format(myy[2],changedd(myy[1]),changed(myy[0])))
            print("너의 덱 : {} {} {}\n".format(yoo[2],changedd(yoo[1]),changed(yoo[0])))
            com(myy[2], yoo[2])
    
    else :
        print("대단한걸! 둘 다 같은 높은 값이나오다니!! 설마해서 여기까진 안만들엇어!")








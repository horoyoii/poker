import tes 
my_money = 11
your_money = 123
sums = 21

print('***최종확인***')

# 족보입력
my_deck= ['♠8','♣2','◆A','♠9','♥7', '♠4','◆3']

your_deck= ['♣7', '♠A', '♠3', '♣8', '♠K', '♣10', '♥J']
myy = tes.jock_bo(my_deck)  # 명칭, 숫자, 문양
yoo = tes.jock_bo(your_deck) # 'TP', 7 ,'t'

print(myy)
print(yoo)

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


def com(a, b) :  #a = '스페', '클로'
    db = ['♠','◆','♥','♣']
    a = 5 - db.index(a)
    b = 5 - db.index(b)
    if a > b :
        print("*** 나 승! ***")
        #sleep(1)
        print("my money : {}".format(my_money+sums))
        print("your money : {}".format(your_money))
    else :
        print("*** 너 승! ***")
        #sleep(1)
        print("my money : {}".format(my_money))
        print("your money : {}".format(your_money+sums))


if myy[0] != yoo[0] :
    print("\n나의 덱 : {}".format(changed(myy[0])))
    print("너의 덱 : {}\n".format(changed(yoo[0])))

    a = tree.index(myy[0])
    b = tree.index(yoo[0])

    if a < b :
        print("*** 나 승! ***")
        #sleep(1)
        print("my money : {}".format(my_money+sums))
        print("your money : {}".format(your_money))
    else :
        print("*** 너 승! ***")
       # sleep(1)
        print("my money : {}".format(my_money))
        print("your money : {}".format(your_money+sums))



else :
    if myy[0] == 'TOP' : # tp, 숫자, 문양 
        if myy[1] != yoo[1] :
            if tree.index(myy[1]) > tree.index(yoo[1]) :
                print("\n나의 덱 :{} {}".format(changedd(myy[1]), changed(myy[0])))
                print("너의 덱 : {} {}\n".format(changedd(yoo[1]), changed(yoo[0])))

                print("*** 나 승! ***")
               # sleep(1)
                print("my money : {}".format(my_money+sums))
                print("your money : {}".format(your_money))

            elif tree.index(myy[1]) < tree.index(yoo[1]) :
                print("\n나의 덱 : {} {}".format(changedd(myy[1]),changed(myy[0])))
                print("너의 덱 : {} {}\n".format(changedd(yoo[1]),changed(yoo[0])))  

                print("*** 너 승! ***")
               # sleep(1)
                print("my money : {}".format(my_money))
                print("your money : {}".format(your_money+sums))

        elif myy[1] == yoo[1] :  
               # 공통으로 쓸 문양 비교 후 결과값 표출함수만들기
            print("\n나의 덱 : {} {} {}".format(myy[2],changedd(myy[1]),changed(myy[0])))
            print("너의 덱 : {} {} {}\n".format(yoo[2],changedd(yoo[1]),changed(yoo[0])))
            print("FF")
            com(myy[2], yoo[2])

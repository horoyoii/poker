import joker



def jock_bo(deck) : # deck = [♠Q ,♥3, ◆J, ♥Q, .♥K, ◆J, ◆J]
    
    lstt = ['RSF', 'BSF', 'SF', 'FC', 'FH', 'Fl', 'MT', 'FS', 'ST', 'TR', 'TP','OP','NO']
    lst = [] # 겹침을 인정하고 deck으로 만들 수 있는 모든 결과를 저장 / 나가서 제일 높은 결과 판별

    #포카드
    #if len(set([i[1] for i in deck])) == 4 : # 포카드
    #    return 'FC'

    # 덱을 뜯어놓기 deck1= ['♠10','◆6','♣A','♣5','♠7', '♠4','♠8']
    d1 = [i[0] for i in deck]  # [◆ ,◆, ◆, ◆, .♥, ◆, ◆]
    d2 = [i[1] for i in deck]  # [2, 2, 2, 2, K, J, J]
    db = ['♠','◆','♥','♣']

    # 로티플, 백스플, 스플, 플 ( 판별 완료 )
    for i in db :
        if d1.count(i) >= 5 :
            ls = [j[1:] for j in deck if j[0]== i] # [10, j, q, k, a, 3]
            #print(ls)  [7 a 3 4 k 2 ]
            lss = set(ls)
            kt = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
            kt1 = ['1','2','3','4','5','6','7','8','9','10','11','12','13']
            if {'10','J','Q','K','A'}.issubset(lss) :
                return 'RSF', i
            if {'5','2','3','4','A'}.issubset(lss) :
                return 'BSF', i

            # 리스트 내의 값 중 연속하는 수가 5개 이상 있음을 판별하는 함수
            # 숫자가 연속됨을 판별하는 식  위 두개 제외 숫자 5개가 연속될 때 STRATE FLUSH
            # ['♠6', '♠2', '♠3', '♠4', '♠5', '♠Q', '♥J'] / lss = {6,2,3,4,5,Q}
            if 'A' in ls : 
              ls[ls.index('A')] = '1' 
            if 'J' in ls :
                ls[ls.index('J')] = '11'
            if 'Q' in ls :
                ls[ls.index('Q')] = '12'
            if 'K' in ls : 
                ls[ls.index('K')] = '13'
            lsss = [int(i) for i in ls]
            lsss.sort()
            
            for q in lsss :
                if q < 10 :
                    a = []
                    for j in range(5) :
                        a.append(q+j)
                    if set(a).issubset(set(lsss)) :
                        return  'SF', i 
                elif q >= 10 : # q = 13
                    for j in lsss :
                        if j <= 4 :
                            lsss[lsss.index(j)] = j+13
                    a = []
                    for k in range(5) :
                        a.append(q+k)
                    if set(a).issubset(set(lsss)) :
                        return  'SF', i 

            # 그 외 나머지 같은 문양이 5개 이상인 것은 풀하우스나 포카드와 중첩되지 않으므로 flush 출력
            return 'FL', i

    # 포카드 판별
    d2 = [i[1:] for i in deck]  # [Q, 3, j, Q, K, J, J]
    ls = [i for i in d2]
    # deck1= ['♠2','◆2','♥2','♣K','♠4', '♠K','♠5'] 
    lss= []
    #print(55)
    #print("22")
    for z in ls :
        if  z == "A" : 
            lss.append(1)
            continue
        if z == "J" :
            lss.append(11)
            continue
        if z == "Q" :
            lss.append(12)
            continue
        if z == "K" : 
            lss.append(13)
            continue
        lss.append(int(z))
    print(lss)
    for j in lss :
        if lss.count(j) == 4 : # j = 2 
            
            return 'FC', j   # 포카드 경우 숫자 반환해줌

    ## 연속수 : 마운트 or 스트레이트 or 백스트레이트 vs 페어 : 풀하우스(2,3) or 트리플(3) or 투페어(2,2) or 원페어(2)
    
    # 풀하우스 판별 - 마 - 백 - 스   -트 - 투 - 원 - none 순으로 판별식 세우기  
    '''
    d1 = [i[0] for i in deck]  # [◆ ,♥, ♠, ◆, .♥, ◆, ◆]
    d2 = [i[1] for i in deck]  # [2, 2, 2, k, K, 4, J]
    db = ['♠','◆','♥','♣']
    '''
    # 같은 수가 4개인 경우는 풀하우스에서 걸러짐
    # 풀하우스 최소조건 : 같은 수가 3개다.
    # lsss = [2,2,2,4,13,5,13]

    ### 풀하우스 
    
    for i in lss :
        if lss.count(i) == 3 :
            ct = [j for j in lss if j != i]  # [4,13,5,13]
            print(ct)
            for k in ct :
                if ct.count(k) == 2 :
                    return "FH", i > k and i or k
    print(lss) # [1, 2, 1, 12, 11, 13, 10] / 10 11 12 13 1
    ## 마운틴
    if {10,11,12,13,1}.issubset(set(lss)) :
        if lss.count(1) == 1:
            return "MT", d1[lss.index(1)]  # A가 하나일 경우
        else :                              # A가 두개 이상일 경우
            db = ['♠','◆','♥','♣']
            num = 0
            dbb =[]             # 1에 해당하는 index값 찾고
            for j in lss :
                if j == 1:
                    dbb.append(num)
                num +=1 
            kt = []
            for z in dbb :
                kt.append(d1[z])
            return "MT", joker.joker(kt) # joker모듈 만들고 joker함수 가져오기 : 무늬 더 큰거 반환

    ## 백스트레이트
    if {1,2,3,4,5}.issubset(set(lss)) :
        if lss.count(1) == 1:
            return "BS", d1[lss.index(1)]  # A가 하나일 경우
        else :                              # A가 두개 이상일 경우
            db = ['♠','◆','♥','♣']
            num = 0
            dbb =[]             # 1에 해당하는 index값 찾고
            for j in lss :
                if j == 1:
                    dbb.append(num)
                num +=1 
            kt = []
            for z in dbb :
                kt.append(d1[z])
            return "BS", joker.joker(kt) # joker모듈 만들고 joker함수 가져오기 : 무늬 더 큰거 반환

    ## 스트레이트 수와 & 문양
    for q in lss : # lss = [9,8,6,5,7,1,2]
        a = []
        for j in range(5) :
            a.append(q+j)
        if set(a).issubset(set(lss)) :
            db = ['♠','◆','♥','♣']
            num = 0
            dbb =[]             # 1에 해당하는 index값 찾고
            for jj in lss :
                if jj == i:
                    dbb.append(num)
                num +=1 
            kt = []
            for z in dbb :
                kt.append(d1[z])
            return  'ST', q+4, joker.joker(kt) 

    ## 트리플
    #print(lss)

    for i in lss :
        if lss.count(i) == 3 :
            return "TR", i
    
    ## 투페어 원페어
    
    for i in lss : #[10, 10, 5, 7, 7, 5, 8]
        if lss.count(i) == 2 :
            ct = [j for j in lss if j != i]
            for k in ct :
                if ct.count(k) == 2 :
                    ctt = [j for j in lss if j != k]
                    for j in ctt :
                        if ct.count(j) == 2 :
                            # i = 10, k = 7, j = 5
                            ss = [i, k, j]
                            if 1 in ss :
                                db = ['♠','◆','♥','♣']
                                num = 0
                                dbb =[]             # 1에 해당하는 index값 찾고
                                for jj in lss :
                                    if jj == 1:
                                        dbb.append(num)
                                    num +=1 
                                kt = []
                                for z in dbb :
                                    kt.append(d1[z])

                                return "TP", 1, joker.joker(kt)

                            else :
                                ss.remove(min(ss))
                                db = ['♠','◆','♥','♣']
                                num = 0
                                dbb =[]             # 1에 해당하는 index값 찾고
                                for jj in lss :
                                    if jj == max(ss):
                                        dbb.append(num)
                                    num +=1 
                                kt = []
                                for z in dbb :
                                    kt.append(d1[z])

                                return "TP", max(ss), joker.joker(kt)
                    # i, k   
                    ss = [i, k]
                    if 1 in ss :
                        db = ['♠','◆','♥','♣']
                        num = 0
                        dbb =[]             # 1에 해당하는 index값 찾고
                        for jj in lss :
                            if jj == 1:
                                dbb.append(num)
                            num +=1 
                        kt = []
                        for z in dbb :
                            kt.append(d1[z])

                        return "TP", 1, joker.joker(kt)

                    else :
                        db = ['♠','◆','♥','♣']
                        num = 0
                        dbb =[]             # 1에 해당하는 index값 찾고
                        for jj in lss :
                            if jj == max(ss):
                                dbb.append(num)
                        num +=1 
                        kt = []
                        for z in dbb :
                            kt.append(d1[z])

                        return "TP", max(ss), joker.joker(kt)


                    db = ['♠','◆','♥','♣']
                    num = 0
                    dbb =[]             # 1에 해당하는 index값 찾고
                    for jj in lss :
                        if jj == max(ss):
                            dbb.append(num)
                        num +=1 
                    kt = []
                    for z in dbb :
                        kt.append(d1[z])
                    return "TP", max(ss), joker.joker(kt)         
            db = ['♠','◆','♥','♣']
            num = 0
            dbb =[]             # 1에 해당하는 index값 찾고
            for jj in lss :
                if jj == i:
                    dbb.append(num)
                num +=1 
            kt = []
            for z in dbb :
                kt.append(d1[z])               
            return "OP", i, joker.joker(kt)

    ## Top 계산
    if 1 in lss :
        return "TOP", 1, d1[lss.index(1)]
    else :
        return "TOP", max(lss), d1[lss.index(max(lss))] # top, 3, 문양
    

                
    


    








deck= ['♠Q', '♥3', '◆J', '♥3', '♥K', '♠2', '♥J']
deck1= ['♥A', '♠J', '♣9', '◆8', '♠7', '♣5', '♠9']
deck2= ['♥9', '♠8', '◆A', '◆5', '♠2', '♠7', '♠A']
deck3= ['♠6', '♠A', '♠3', '♠4', '♠5', '♠7', '♥J']
lstt = ['RSF', 'BSF', 'SF', 'FC', 'FH', 'Fl', 'MT', 'FS', 'ST', 'TR', 'TP','OP','NO']
lst = []
print("TT")
print(jock_bo(deck1))
print(jock_bo(deck2))
print(type(jock_bo(deck3)))
#print([i[1] for i in deck if i[0]=='♥'])
'''
lsttt = ['1','2','3','5','3','K','Q','J']

print(sorted(lsttt))


print({1,6,4}.issubset({1,2,3,4,5,6}))

k = [1,2,3,4,5,6,7,8,9,10]

t = [5,3,6,7]
t.sort()
print(t == k[k.index(t[0]): k.index(t[0])+len(t)])
## 연속하느냐 판별
tt = [1,2,3,5]

tt[tt.index(2)] = 1


print(tt)
'''



#[1,3,4,5,6,7,10,11]
#[k,1,2,3,4] # 돌려서 k기준 (k=13) 13 14 15 16 17 이라면 14 = 1
# 값을 하나씩가져옴 / 그 값에 +1씩 해준 값들을 5개까지 만듬 / 만들어진 리스트를 세트화 / 이 세트가 초기세트의 부분집합인가 boolen  
#                   가져온 값이 10이상일 때 초기세트의 1,2,3,4 를 14,15,16,17 로 변환한 후 부분집합 판별

for i in [int(i) for i in ['1','2']] :
    print(i)
a = {3,4,5}
a.add(1)
print(a)
ls = [1,2,3,4,4]
lss = [1,2]
print(set(ls))

if set(lss).issubset(set(ls)) :
    print('2')

ls =['A']
ls[ls.index('A')] = '1'
print(ls)

import numpy as np

lst = [[1,2,3],[4,5,6],[0,8]]
s1 = np.array(lst)

print(s1)

print(all(s1))
""" a = [1,2,3,['a','v','c']]

 a = [1,2,3,4,5]

 a.reverse() #54321
 a.sort #12345
 a.sort(reverse = True)
 a.index(3)
 a.append(4) #맨마지막에 숫자4넣어줌

 #튜플 삭제 수정불가,요소 1개만 가질때 (1,)해줌
 #딕셔너리
 a = {'a':[1,2,3]}"""
'''while 1:
    n = int(input())
    sum = 0
    if n<1 or n>10000:
        print("숫자를 다시입력하세요 : ")
        continue
    for i in range(1,n+1):  
        if i % 3 == 0:
            sum = sum + i
    print(sum)'''
'''a = [70,60,55,75,95,80,80,85,100]
sum=0
count=0
for i in a :
    sum = sum+i
print(sum/len(a))'''
    
            
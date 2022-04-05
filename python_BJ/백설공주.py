# 왕비를 피해 일곱 난쟁이들과 함께 평화롭게 생활하고 있던 백설공주에게 위기가 찾아왔다. 일과를 마치고 돌아온 난쟁이가 일곱 명이 아닌 아홉 명이었던 것이다.
# 아홉 명의 난쟁이는 모두 자신이 "백설 공주와 일곱 난쟁이"의 주인공이라고 주장했다. 뛰어난 수학적 직관력을 가지고 있던 백설공주는, 다행스럽게도 일곱 난쟁이의 키의 합이 100이 됨을 기억해 냈다.
# 아홉 난쟁이의 키가 주어졌을 때, 백설공주를 도와 일곱 난쟁이를 찾는 프로그램을 작성하시오.

littleBoy = [] #난쟁이 9명의 키를 담을 리스트
result = 0 # 난쟁이 키의 합을 담을 변수

for i in range(1,10): #난쟁이 9명의 키를 입력받아 리스트에 추가
    a = int(input())
    littleBoy.append(a)
    result += a

result -= 100 # 7난쟁이 키의 합인 100을 빼줌
littleBoy.sort() # 작은수부터 정렬

def check(): # 가짜난쟁이 2명을 판단하는 함수
    for i in range(len(littleBoy)): # 2중 for문으로 완전탐색 시작
        for j in range(i+1,9):
            if littleBoy[i] + littleBoy[j] == result: # 가짜 난쟁이 2명 키의 합 찾는 조건문
                del littleBoy[j] # 앞쪽 인덱스부터 삭제하면 뒤쪽 인덱스가 바뀌므로 뒤쪽부터 삭제
                del littleBoy[i]
                return littleBoy
            else:
                continue


check()
littleBoy.sort()
for i in littleBoy:
    print(i)

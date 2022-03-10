non_selfnumber = [] # 셀프넘버가 아닌 수를 담는 리스트

def distinguis(a): #셀프넘버인지 판별하는 함수
    result = 0 # non_selfnumber를 담을 변수
    number = str(a) # 정수 a를 문자열로 변경 <- 한자리씩 계산하기 위해서
    result += int(number)

    for i in number: #number를 한자리씩 떼서 계산
        result += int(i)

    non_selfnumber.append(result) # 리스트에 result 추가

for i in range(1,10001):
    distinguis(i) #1부터 10000까지 non_selfnumber 리스트 생성

for i in range(1,10001):
    if i not in non_selfnumber: #non_selfnumber 리스트에 없는 숫자이면 출력
        print(i)


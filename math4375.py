#2와 5로 나누어 떨어지지 않는 정수 n(1 ≤ n ≤ 10000)가 주어졌을 때, 1로만 이루어진 n의 배수를 찾는 프로그램을 작성하시오.

while True: # while을 사용한 무한반복문이다
    try: #TESTCASE의 갯수를 모르므로, try, except를 사용
        n = int(input())

        check_str = "1" # 1이 몇개가 필요한지 판별할 문자열 생성

        while True:
            if int(check_str) % n != 0: #n으로 나눠떨어지지 않으면
                check_str += "1" # 문자열에 1 추가 (1-> 11 -> 111 ...)

            else:   #n으로 나누어 떨어진다면
                print(len(check_str)) #문자열의 길이 출력 -> 1의 개수
                break
    except: # try속 코드에서 에러가 발생하면 프로그램이 멈추지 않고, except로 이동한다.
        break

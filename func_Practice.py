i_list = list(map(int,input().split())) # 띄워쓰기로 나눠서 입력받고, 입력 받은 문자열을 정수로 변환시켜 리스트에 넣어줌


def solve(a):
    ans = 0
    for i in a:
        ans += i

    return ans

print(solve(i_list))

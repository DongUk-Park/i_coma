Testcase = int(input())

for test in range(Testcase):
    H,W,N = map(int,input().split())

    floor = 0
    count = 0
    x = 0

    if H == 1: # 예외처리 : 층수가 1층이면 N번째 방을 준다
        if N>=10:
            print(f"1{N}")
        else:
            print(f"10{N}")
    else:
        for i in range(1,N):
            if H*i >= N: # 높이 * x + 들어가야 할 floor = N(번째 사람)
                x = i-1 # x-1을 x에 넣는다
                break

        floor = N - x*H # 위에서 구한 x로 N번째 사람이 몇층에 들어 가야 하는지 구함
        x += 1 # x에 x-1이 들어갔으므로 다시 1을 더해 x로 만들어준다

        if x>=10:
            print(f"{floor}{x}")
        else:
            print(f"{floor}0{x}")


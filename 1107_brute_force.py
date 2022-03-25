# 수빈이는 TV를 보고 있다. 수빈이는 채널을 돌리려고 했지만, 버튼을 너무 세게 누르는 바람에, 일부 숫자 버튼이 고장났다.
# 리모컨에는 버튼이 0부터 9까지 숫자, +와 -가 있다. +를 누르면 현재 보고있는 채널에서 +1된 채널로 이동하고, -를 누르면 -1된 채널로 이동한다. 채널 0에서 -를 누른 경우에는 채널이 변하지 않고, 채널은 무한대 만큼 있다.
# 수빈이가 지금 이동하려고 하는 채널은 N이다. 어떤 버튼이 고장났는지 주어졌을 때, 채널 N으로 이동하기 위해서 버튼을 최소 몇 번 눌러야하는지 구하는 프로그램을 작성하시오.
# 수빈이가 지금 보고 있는 채널은 100번이다


target = int(input())

result = abs(100 - target) # ++ , -- 만으로 이동했을때의 값

count_broken_button = int(input()) #부숴진 버튼 개수

if count_broken_button: # 고장난게 있을 때
    broken_buttons = set(input().split()) # 고장난 버튼을 set 으로 받아온다
else:
    broken_buttons = set()


for num in range(1000001): #큰수->작은수 하기 위해선 100만까지 필요하다.
    num = str(num)
    for i in range(len(num)):
        if num[i] in broken_buttons:
            break
        elif i == len(num) - 1: #마지막 인덱스까지 부숴진 버튼이 없다면
            num = int(num)
            result = min(result, len(str(num)) + abs(num - target)) # (result, num번호를 입력한 횟수 + num과 target사이를 count)

print(result)


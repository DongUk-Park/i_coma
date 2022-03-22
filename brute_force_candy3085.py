# 상근이는 어렸을 적에 "봄보니 (Bomboni)" 게임을 즐겨했다.
# 가장 처음에 N×N크기에 사탕을 채워 놓는다. 사탕의 색은 모두 같지 않을 수도 있다. 상근이는 사탕의 색이 다른 인접한 두 칸을 고른다. 그 다음 고른 칸에 들어있는 사탕을 서로 교환한다. 이제, 모두 같은 색으로 이루어져 있는 가장 긴 연속 부분(행 또는 열)을 고른 다음 그 사탕을 모두 먹는다.
# 사탕이 채워진 상태가 주어졌을 때, 상근이가 먹을 수 있는 사탕의 최대 개수를 구하는 프로그램을 작성하시오.

# 브루트포스 문제로, 모든 경우의 수를 확인해야한다. 모든 행과 열에서 상하좌우를 바꿀 필요없이, 양옆으로 한번, 위아래로 한번이면 상하좌우가 한번씩 바뀐다



n = int(input()) # n x n 의 사탕 배열 <- 여기의 n

arr = [list(input()) for _ in range(n)] # 문자열 여러개를 리스트의 형태로 입력 받음

def check(arr): # 가장 많이 연속되는 사탕의 개수를 return 해주는 함수
    v = len(arr) # 행의 개수
    result = 1 # return 할 변수
    
    for i in range(v):
        #열을 순회하면서 연속되는 숫자 세기
        count = 1 # 연속되는 숫자의 개수를 넣을 공간

        for j in range(1,n):
            if arr[i][j] == arr[i][j-1]: #이전 열과 같다면
                count += 1
            else: #이전과 다르다면 1로 초기화
                count = 1

            if count >= result: #최대값으로 계속 업데이트 시켜줌
                result = count

        count = 1
        for j in range(1, n):
            #행을 순회하면서 연속되는 숫자 세기
            if arr[j][i] == arr[j-1][i]: #이전 행과 같다면 count 에 1 더하기
                count += 1
            else:  # 이전과 다르다면 1로 초기화
                count = 1

            if count >= result:  # 최대값으로 계속 업데이트 시켜줌
                result = count

    return result


answer = 0 # 최종 결과를 담을 변수

for i in range(n):
    #열에서 인접한 것 끼리 바꾸기
    for j in range(n): #모든 경우의 수를 확인하기 위해 모든 열과 행에 있는 수를 한번씩 바꿔줌
        if j+1 < n:
            arr[i][j] , arr[i][j+1] = arr[i][j+1] , arr[i][j]

            tmp = check(arr) #임의의 공간에

            if answer < tmp:
                answer = tmp

            arr[i][j], arr[i][j + 1] = arr[i][j + 1], arr[i][j] #바꿨던 것 다시 돌려놓기기

        if i+1 < n:
            arr[i][j] , arr[i+1][j] = arr[i+1][j] , arr[i][j]

            tmp = check(arr) #임의의 공간에

            if answer < tmp:
                answer = tmp

            arr[i][j] , arr[i+1][j] = arr[i+1][j] , arr[i][j]

print(answer)













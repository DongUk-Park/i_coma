#자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.
#1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열

n,m = map(int,input().split())

visited = []

def check():
    #맨 위에는 탈출조건
    if len(visited) == m: #원하는 만큼 탐색을 했다면
        print(' '.join(map(str,visited)))
        return

    for i in range(1,n+1): #1 부터 n까지
        if i not in visited: # i가 visited 안에 없다면
            visited.append(i)
            check() #재귀
            visited.pop()

check()
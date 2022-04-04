import itertools

n,m = map(int, input().split())
arr = []

for i in range(n):
	arr.append(i+1)


com = list(itertools.combinations(arr, 2))

for ele in com:
	print(ele)

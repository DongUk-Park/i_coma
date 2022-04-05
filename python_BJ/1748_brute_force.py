n = int(input())

len_n = len(str(n)) # n의 자릿수 파악( ex 123 : 3자릿수)

sum = 0

for i in range(len_n-1):
    sum += 9 * (10 ** i) * (i+1) # ex)3자릿수라면(123) 두자릿수까지의 경우의수 계산

nums = n - (10 ** (len_n-1)) + 1 # ex) 3자리수라면 n - 100 +1 을 통해 100~n 사이의 개수 구하기
sum += nums * len_n # ex) 3자릿수 개수 * 3 -> 세자릿수 숫자들의 길이

print(sum)



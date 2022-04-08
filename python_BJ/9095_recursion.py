#정수 n이 주어졌을 때, n을 1, 2, 3의 합으로 나타내는 방법의 수를 구하는 프로그램을 작성하시오.

TestCase = int(input())

def check(n):  # 규칙 : n의 경우의수 : n-1 경우의수 + n-2 경우의수 + n-3 경우의수

    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    else:
        return check(n-1) + check(n-2) + check(n-3)


for i in range(TestCase):
    n = int(input())
    print(check(n))



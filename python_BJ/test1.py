a,b,c = input().split() #한번에 여러개의 입력을 받기 위해 .split()
a = int(a)
b = int(b)
c = int(c) # 파이썬은 입력을 받을 때 문자열로 입력을 받기 때문에 int로 형변환

if a>b:
    print(">")

elif a==b:
    print("==")

else:
    print("<")

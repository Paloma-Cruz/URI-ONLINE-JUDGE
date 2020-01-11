a, b, c = input().split(" ")
a = int(a)
b = int(b)
c = int(c)

if a > b and a > c:
    print('%i eh o maior' %a)
elif b > a and b > c:
    print('%i eh o maior' %b)
else:
    print('%i eh o maior' %c)

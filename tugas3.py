x = int(input())
y = int(input())
z = int(input())
a = max(x, y, z)
b = min(x, y, z)
if a > x > b :
    print(x)
if a > y > b :
    print(y)
if a > z > b :
    print(z)
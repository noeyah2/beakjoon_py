a = int(input())    #문자열로
b = input()
print(a * int(b[2]))    #반복문 없이
print(a * int(b[1]))
print(a * int(b[0]))
print(a * int(b))

for i in range(3,0,-1): #반복문 사용
    print(a * int(b[i,-1]))
print(a * int(b))
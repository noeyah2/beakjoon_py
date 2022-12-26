h,m = map(int, input().split())
timer = int(input())
h += timer//60  #h = h+timer
m += timer%60   #m = m+timer
if m >= 60:
    h += 1  #h = h+1
    m -= 60 #m = m-60
elif h >= 24:
    h -= 24
print(h,m)
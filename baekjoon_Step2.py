'''1330번
a,b = input().split()
a = int(a)
b = int(b)
if(a<b):
    print("<")
elif(a>b):
    print(">")
else:
    print("==")'''

'''9498번
score = int(input())
if(score>=90):
    print("A")
elif(score>=80):
    print("B")
elif(score>=70):
    print("C")
elif(score>=60):
    print("D")
else:
    print("F")'''

'''2753번
year =int(input())
if(year%4==0 and (year%100 != 0 or year%400 == 0)):
    print(1)
else:
    print(0)'''

'''14681번
x = int(input())
y = int(input())
if(x>0 and y>0):
    print(1)
elif(x>0 and y<0):
    print(4)
elif(x<0 and y>0):
    print(2)
else:
    print(3)'''

'''2884번
h, m = input().split()
h = int(h)
m = int(m)

if(m >= 45):
    print(h,m-45)
else:
    if(h==0):
        print(23,60-(45-m))
    else:
        print(h-1,60-(45-m))'''

'''2525번'''
now_h, now_m = input().split()
now_h = int(now_h)
now_m = int(now_m)
m = int(input())

if(now_m + m<= 60):
    print(now_h,now_m+m)
else:
    fin_h =now_h+(now_m+m)//60
    if(fin_h >=24):
        print(fin_h - 24,(now_m+m)%60)
    else:
        print(fin_h,(now_m+m)%60)
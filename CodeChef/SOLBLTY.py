t=int(input())
for i in range(t):
    x,a,b=map(int,input().split())
    z=((100-x)*b)+a
    print(z*10)

t=int(input())
for i in range(t):
    a1,a2=map(int,input().split())
    b1,b2=map(int,input().split())
    c1,c2=map(int,input().split())
    z=a1+a2
    y=b1+b2
    x=c1+c2
    print(max(x,y,z))

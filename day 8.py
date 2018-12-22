n=int(input())
b=dict()
for _ in range(n):
    a=input().split()
    b[a[0]]=int(a[1])
for _ in range(n):
    a=input()
    if a not in b.keys():
        print('Not found')
    else:
        print(a+'='+str(b[a]))
        
    
    
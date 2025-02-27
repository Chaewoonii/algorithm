winnings = 0
for _ in range(int(input())):
    cnt = {}
    for n in list(map(int, input().split())):
        cnt[n] = 1 if n not in cnt.keys() else cnt[n] + 1

    temp = {v:k for k, v in cnt.items()}

    if len(cnt) == 1:
        winnings = max(winnings, 50000 + (temp[4] * 5000)) #1

    elif len(cnt) == 2:
        if max(cnt.values()) == 3:
            winnings = max(winnings, 10000 + (temp[3] * 1000)) #2

        elif max(cnt.values()) == 2:
            winnings = max(winnings, 2000 + sum(k * 500 for k in cnt.keys())) #3

    elif len(cnt) == 3:
        winnings = max(winnings, 1000 + (temp[2] * 100)) #4

    elif len(cnt) == 4:
        winnings = max(winnings, max(cnt.keys()) * 100) #5

print(winnings)

'''
print(max([d,10+[c,b][c<d],5*[20+b*2,4+a+c][b<c],500+a*50][-len({a,b,c,d})]for i in[*open(0)][1:]for(a,b,c,d)in[sorted(map(int,i.split()))])*100)

import sys
input=sys.stdin.readline
ans=0
for _ in range(int(input())):
    a,b,c,d=sorted(map(int,input().split()))
    s={a,b,c,d}
    if len(s)==1:
        ans=max(50000+a*5000,ans)
    elif len(s)==2:
        if b==c:
            ans=max(10000+b*1000,ans)
        else:
            ans=max(2000+500*(b+c),ans)
    elif len(s)==3:
        t=c
        if a==b:
            t=b
        ans=max(1000+t*100,ans)
    else:
        ans=max(d*100,ans)
print(ans)
'''
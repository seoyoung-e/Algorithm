n=int(input())
cnt=4
for k in range(1,n+1):
    x=2**k*(2**(k-1)+1)  + 4**(k-1)
    cnt+=x
print(cnt)
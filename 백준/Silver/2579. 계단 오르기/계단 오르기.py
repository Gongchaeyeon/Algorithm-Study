import sys
n = int(sys.stdin.readline().strip())
arr=[]
dp=[0]*(n)

for i in range(n):
    arr.append(int(sys.stdin.readline().strip()))

if n<=2:
    print(sum(arr))
else:
    dp[0] = arr[0]
    dp[1] = arr[0] + arr[1]
    for i in range(2,n):
        dp[i] = max(dp[i-3]+arr[i-1]+arr[i] , dp[i-2]+arr[i])
    print(dp[-1])
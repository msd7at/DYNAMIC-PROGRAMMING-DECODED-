#https://www.hackerearth.com/problem/algorithm/utkarsh-and-jumps/editorial/
# not working there but code is fine
n,p=map(int,input().split())
d=[]
d.append(1)
d.append(0)
d.append(p/100.0)
d.append(1-(p/100.0))
for i in range(4,n+1):
    d.append((p/100.0)*(d[i-2]+(1-(p/100.0)*d[i-3])))
print('%.6f'%d[n])
# print(d[n])


# AUTHORS SOLUTION 

#include<bits/stdc++.h>
#include<iostream>
using namespace std;
#define fre 	freopen("0.in","r",stdin),freopen("0.out","w",stdout)
#define abs(x) ((x)>0?(x):-(x))
#define M 1000000007
#define lld signed long long int
#define pp pop_back()
#define ps(x) push_back(x)
#define mpa make_pair
#define pii pair<int,int>
#define fi first
#define se second
#define scan(x) scanf("%d",&x)
#define print(x) printf("%d\n",x)
#define scanll(x) scanf("%lld",&x)
#define printll(x) printf("%lld\n",x)
#define boost ios_base::sync_with_stdio(0)
//vector<int> g[2*100000+5];int par[2*100000+5];
double dp[1000000+5];
int main()
{
	freopen("input-9.txt","r",stdin);
   freopen("output-9.txt","w",stdout);
	int N,P;
	cin>>N>>P;
	dp[0]=1;
	dp[1]=0;
	dp[2]=P/100.0;
	dp[3]=1 - P/100.0;
	for(int i=4;i<=N;++i)
	{
		dp[i]=(P/100.0)*dp[i-2] + (1-P/100.0)*dp[i-3];
	}
	printf("%0.6f",dp[N]);
}

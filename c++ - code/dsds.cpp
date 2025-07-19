
#include<bits/stdc++.h>
using namespace std;
int main()
{
    int a[2000000];
    int n;
    int maxx=-10000000;
    cin>>n;
    for(int i=1;i<=n;i++)
        cin>>a[i];
    for(int i=1;i<=n;i++){
        int num=0;
        for(int j=i;j<=n;j++){
            num+=a[j];
            if(num>maxx)
                maxx=num;
        }
    }
    cout<<maxx;

}

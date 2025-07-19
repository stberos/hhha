#include<bits/stdc++.h>
using namespace std;
int n;
vector<int>a;
vector<int>b;
vector<int>c;
int main()
{
    cin>>n;
    int y;
    for(int i=1;i<=n;i++)
    {
        cin>>y;
        a.push_back(y);
        b.push_back(y);
    }
    sort(a.begin(), a.end(), greater<int>());
    for(int i=0;i<a.size();i++)
        for(int j=0;j<a.size();j++)
        {
            if(b[i]==a[j])
                c.push_back(i+1);
        }
    for(int i=0;i<a.size()-1;i++)
    {
        if(a[i]==a[i+1])
            c[i+1]=c[i];
    }
    for(int i=0;i<c.size()-1;i++)
        cout<<c[i]<<endl;


}

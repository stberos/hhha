
#include<bits/stdc++.h>
using namespace std;
string s,p;
int main()
{

    cin >> s >> p;
    bool d=true;
    for(int i=0;i<p.length();i++)
    {
        if(p[i]=='*')
            continue;
        for(int j=i;j<s.length();j++)
        {
            if(s[j]==p[i])
                break;
            else
            {
                if(j==s.length()-1)
                    d= false;
            }
        }

    }
    if(d==true)
        cout<<"true";
    else
        cout<<"false";
}

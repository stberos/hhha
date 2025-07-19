//
// Created by bondli on 25-2-6.
//
// 更规范的写法（不推荐用<bits/stdc++.h>）
#include <iostream>
#include <string>
using namespace std;

int main() {
    string n;
    cin >> n;

    // 检查字符串长度是否 >=1（允许插入位置1）
    if (n.size() >= 1) {
        n.insert(1, "e");  // 安全插入
    } else {
        cout << "输入字符串太短！" << endl;
    }

    cout << n;
    return 0;
}

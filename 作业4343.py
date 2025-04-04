n=int(input("请输入所求的月份值:"))
a=1
b=1
for i in range(3,n+1):
    t=a+b
    a=b
    b=t
print("%d月兔子有%d对"%(n,t))

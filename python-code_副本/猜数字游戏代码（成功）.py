from random import randint
# 导入可以随机生成数的库
def guess_number(start = 1 , end = 10 , times = 3):
    # 定义函数，def是关键字，guess_number是函数名称
    # start，end，times是带默认值的形参，若调用函数时没有传递实参，就用默认值
    number = randint(start , end)
    # 生成指定范围的随机数，也就是要猜的数
    # 用for循环控制最大猜测次数，如果次数用完仍未猜对就结束循环
    for i in range(times):
        # 关键字else的用法1：value1 if condition else value2，condition值为真取value1，否则取value2
        prompt = '开始猜吧，' if i==0 else '再猜一次'
        # f-字符串，把大括号内的表达式替换为对应的计算结果
        prompt = f'剩余{times - i}次，{prompt}[{start},{end}]范围的数是什么：'
        # 接收用户输入，返回字符串
        value = input(prompt)
        try:
            # 异常处理结构，把可能会出错的代码放在try块中
            # 尝试把字符串转换为整数
            value = int(value)
        except:
            print('必须输入整数。',end = '')
        else:
            if value == number:
                print('恭喜，猜对了。')
                return True
            elif value > number:
                print('猜大了。')
            else:
                print('猜小了。')
    else:
        print('次数用完，没有猜对。')
        return False
total , win , times = 0 , 0 , 3
while True:
    # 玩游戏的次数
    total = total + 1
    start = randint(1 , 100)
    end = randint(start , start + 30)
    if guess_number(start , end , times = times):
        win = win + 1
        times = times + 1
    else:
        times = times - 1
    if times <= 0:
        print('最大猜测次数已经变成0了，不允许再玩了。')
        break
    # 必须输入Y或者N
    while True:
        flag = input('还想再来一局吗？(Y/N)：').upper()
        if flag in ('Y','N'):
            break
    if flag == 'N':
        break
print(f'{"="*10}\n一共玩了{total}局，赢了{win}局。')



# 猜数字基本代码框架

# import random 
# num = random.randint(0, 100)
# num1 = None
# while num1 != num:
#     num1 = int(input("请输入："))
#     if num1 > num:
#         print("*****你再猜小一点。*****")
#     elif num1 < num:
#         print("*****你再猜大一点。*****")
#     else: 
#         break

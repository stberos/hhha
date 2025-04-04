class Animal:
    def __init__(self,name,weight,legNum):
        self.name = name
        self.weight = weight
        self.legNum = legNum
ostrich  = Animal("鸵鸟",190,4)
print("我是一只鸵鸟，我的名字是:%s,重量是%dkg，有%d条腿"%(ostrich.name,ostrich.weight,ostrich.legNum))

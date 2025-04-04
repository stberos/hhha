class Animal:
    def __init__(self,name,weight,legNum):
        self.name = name
        self.weight = weight
        self.legNum = legNum
tiger = Animal("山大王",190,4)
print("我是一只老虎，我的名字是:%s,重量是%dkg，有%d条腿"%(tiger.name,tiger.legNum,tiger.legNum))

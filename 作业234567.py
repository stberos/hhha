class Bird:
    def __init__(self,color):
        self.color=color
    def say(self):
        print("一只%s的小鸟在叽叽喳喳的叫"%self.color)
b=Bird("红色")
b.say()
class Parrot(Bird):
    def say(self,words):
        print("一只%s的鹦鹉在说:%s"%(self.color,words))
        
b=Parrot("红色")
b.say("你好")

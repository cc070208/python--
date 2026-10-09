class Dg():
    def __init__(self):
        self.cook_time=0
        self.cook_state='生的'
        self.condiment=[]


    def cook(self,time):
        if time<0:
            print("输入错误")
        else:
            self.cook_time+=time
            if 0<=self.cook_time<3:
                self.cook_state='生的'
            elif 3<=self.cook_time<7:
                self.cook_state='半生不熟的'
            elif 7<=self.cook_time<12:
                self.cook_state='熟了'
            else:
                print("糊了")


    #不定长参数*args会将剩下的数据打包成元组，可通过解包
    def add_condiment(self,*args):
        for item in args:
            self.condiment.append(item)
            
    def __str__(self):
        return f'烘烤时间：{self.cook_time},状态：{self.cook_state},调料:{self.condiment}'
    

    
dg = Dg()
dg.cook(1)
dg.cook(3)
dg.cook(7)
dg.add_condiment("辣椒",1)
dg.add_condiment("折耳根",2)

print(dg)




            

from threading import *
class Multiplication:
    def Mul(self,num):
        for i in range(1,6):
            print(num,'X',i,'=',num*i)
class MyThread(Thread):
    def __init__(self,tableobj,num):
        Thread.__init__(self)
        self.tableobj=tableobj
        self.num=num
    def run(self):
        threadlock.acquire()
        self.tableobj.Mul(self.num)
        threadlock.release()
threadlock=Lock()
tableobj=Multiplication()
t1=MyThread(tableobj,2)
t2=MyThread(tableobj,3)
t1.start()
t2.start()
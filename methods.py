import numpy as np
import math
class ex2:
    def __init__(self,a):
        self.a=a
    def make_ex2(self,a):
        a=np.arange(100,200,10)
        print(a)
class ex3:
    def __init__(self,a):
        self.a=a
    def make_ex3(self,a):
        print(a[:,2])
class ex4:
    def __init__(self,a):
        self.a=a
    def make_ex4(self,a):
        print(a[::2 , 1::2])
class ex5:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def make_ex5(self,a,b):
        c=a+b
        c=np.sqrt(c)
        print(c)
class ex6:
    def __init__(self,a):
        self.a=a
    def make_ex6(self,a):
        a=np.sort(a)
        print(a)
class ex7:
    def __init__(self,a):
        self.a=a
    def make_ex7(self,a):
        min=a.min(axis=1)
        max=a.max(axis=0)
        print("Min is: ",min,", Max is: ",max)
class ex8:
    def __init__(self,a,c):
        self.a=a
        self.c=c
    def make_ex8(self,a,c):
        a=np.delete(a,1,0)
        a=np.insert(a, 1, c, 0)
        print(a)
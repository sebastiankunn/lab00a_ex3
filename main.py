import numpy as np
from methods import *
if __name__ == '__main__':
    exer=input("Select an exercise\n")
    match exer:
        case '1':
            a = np.zeros((4, 2))
            print(a)
        case '2':
            a=np.zeros((5,2))
            ex=ex2(a)
            ex.make_ex2(a)
        case '3':
            a=np.array([[11 ,22, 33], [44, 55, 66], [77, 88, 99]])
            ex=ex3(a)
            ex.make_ex3(a)
        case '4':
            a=np.array([[3 ,6, 9, 12], [15 ,18, 21, 24], [27 ,30, 33, 36], [39 ,42, 45, 48], [51 ,54, 57, 60]])
            ex=ex4(a)
            ex.make_ex4(a)
        case '5':
            a=np.array([[5, 6, 9], [21 ,18, 27]])
            b=np.array([[15 ,33, 24], [4 ,7, 1]])
            ex=ex5(a,b)
            ex.make_ex5(a,b)
        case '6':
            a=np.array([[34,43,73],[82,22,12],[53,94,66]])
            ex=ex6(a)
            ex.make_ex6(a)
        case '7':
            a=np.array([[34,43,73],[82,22,12],[53,94,66]])
            ex=ex7(a)
            ex.make_ex7(a)
        case '8':
            a=np.array([[34,43,73],[82,22,12],[53,94,66]])
            c=np.array([10,10,10])
            ex=ex8(a,c)
            ex.make_ex8(a,c)
import math
import pandas as pd
import numpy as np 

data = pd.read_excel(r'point.xlsx')
matrice = data.iloc[0:,0:8]
matrice = np.matrix(matrice)

def affect(tab):
    a=0
    b=0
    for i in range(tab.shape[0]):
        b+=tab[i,1]
        a+=tab[i,0]
    a=a/tab.shape[0]
    b=b/tab.shape[0]
    return [a,b]

def resul(matrix,c1,c2):
    tab1 =[]
    tab2 =[]
    for i in range(matrix.shape[1]):
        dl1= math.sqrt(pow(matrix[0,i]-c1[0],2)+ pow(matrix[1,i]-c1[1],2))
        dl2= math.sqrt(pow(matrix[0,i]-c2[0],2)+ pow(matrix[1,i]-c2[1],2))
        if dl1<dl2:
            tab1.append([matrix[0,i],matrix[1,i]])
        else:
            tab2.append([matrix[0,i],matrix[1,i]])
    tab1 = np.matrix(tab1)
    tab2 = np.matrix(tab2)
    m1=affect(tab1)
    m2=affect(tab2)
    return(m1,m2,tab1,tab2)

c=([1,1],[2,1])
m=0

while c!=m :
    m=c
    c=resul(matrice,c[0],c[1])
    tab1=c[2]
    tab2=c[3]
    c=c[0:2]

print("Groupe 1: \n",tab1)
print("Groupe 2: \n",tab2)
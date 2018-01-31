import numpy as np
from numpy import array
class decisionnode:
    def __init__(self,value=None,col=None,tb=None,fb=None):
        self.value=value
        self.col=col
        self.tb=tb
        self.fb=fb
        
        
def readdata(filename):    
    data=open(filename).readlines()
    x=[]
    for line in data:
        line=line.strip().split('\t')
        x_i=[]
        for num in line:
            num=float(num)
            x_i.append(num)
        x.append(x_i)
    x=array(x)
    return x
    
def median(x):
    n=len(x)
    x=list(x)
    x_order=sorted(x)
    return x_order[n//2+1],x.index(x_order[n//2+1])
    
def buildtree(x,j):
    tb=[]
    fb=[]
    m,n=x.shape
    if m<=1: return decisionnode(edge=None,row=tb[0])
    edge,row=median(x[:,j].copy())
    print(edge,row)
    print(edge,row)
    for i in range(m):
        if x[i][j]>edge: 
            tb.append(i)
        if x[i][j]<edge:
            fb.append(i)
    tb_x=x[tb,:]
    fb_x=x[fb,:]
    print(tb)
    print(fb)
    if len(tb)>1: trueBranch=buildtree(tb_x,j+1)
    else: trueBranch=decisionnode(edge=None,row=tb[0])
    if len(fb)>1:falseBrach=buildtree(fb_x,j+1)
    else: falseBrach=decisionnode(edge=None,row=fb[0])
    return decisionnode(edge,row,j,trueBranch,falseBrach)
    
            

        
    


from multiprocessing import Pool
import matplotlib.pyplot as plt
import numpy as np
from numpy.linalg import inv
import time
import LRmultiplication
import LRdatainp
if __name__=='__main__':
    pool=Pool()
    x2,y=LRdatainp.getData()
    start=time.time()
    x1=[1]*len(x2)
    multi=[[x1,x1],[x1,x2],[x2,x2],[x1,y],[x2,y]]
    pool=Pool(processes=4)
    ans=pool.map(LRmultiplication.multiply,multi)
    inver=inv(np.array([ans[:2],ans[1:3]]))
    temp=np.array(ans[3:5])
    listW=inver.dot(temp)
    print("the Slope=",listW)
    done=time.time()
    print("Time diff=",done-start)
    plt.scatter(x2[:100],y[:100],color="m",marker="o",s=30)
    x_pred=np.arange(-1000,1000,1)
    plt.plot(x_pred,listW[1]*x_pred+listW[0],color='g')
    plt.axis([0,1000,0,1000])
    plt.ylabel('y-axis')
    plt.xlabel('x-axis')
    plt.show()

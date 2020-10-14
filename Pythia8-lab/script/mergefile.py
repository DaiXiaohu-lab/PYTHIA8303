# -*- coding:utf-8 -*-  
import os
root='D:\\Administrator\\ProgramFile\\PyCharm\\exercise'
path='D:\\Administrator\\ProgramFile\\PyCharm\\exercise\\Select'
files=os.listdir(path) 
result=os.path.join(root,'Select_all.txt') #生成最终txt文件(X_3872.txt)的路径
with open(result,'w') as r:
    for i in range(1,54): 
        print(i) 
        fname=str(i) 
        filename=os.path.join(path,fname) 
        with open(filename,'r') as f: 
            for line in f:
                r.writelines(line)
            r.write('\n')



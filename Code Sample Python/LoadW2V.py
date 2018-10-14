import io
import random
import numpy as np
f_w2v   = '\\Word2Vec.txt';

model = dict({})
f = open(f_model, 'r',encoding="utf-8")

for line in f:
    line = line.strip()
    ww = line.split()
    if (len(ww)>2):
        word = ww[0]
        tem=[]
        try:
            for i in range(1,len(ww)):
                tem.append(float(ww[i]))
            temp = np.array(tem)
        except:
            print('error! ', word)
        model.update({word:temp})       
f.close()

    
    

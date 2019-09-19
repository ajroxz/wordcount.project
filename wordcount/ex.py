import pandas as pd 
from pylab import *
dict = {'MP':[1,2],'UP':[1,0]}
x=[1,2,4,5,66]
y=[3,4,5,5,5]
df = pd.DataFrame(dict)

df.index=[1,2]

print(df)

df.reindex([3,4])
print(df)
de = [13,14]

df['delhi']=de
print(df)

subplot(3,2,1)
title('spd')
plot(x,y)


subplot(2,2,2)
title('dps')
z=plot(y,x)


show()


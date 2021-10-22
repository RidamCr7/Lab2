import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
df_miss=pd.read_csv('landslide_data3_miss.csv')
df_miss


# In[2]:


# Que-1

columns=['dates','stationid','temperature','humidity','pressure','rain','lightavgw/o0','lightmax','moisture']
B=[]
x=np.arange(len(columns))
df_miss.fillna("Missing",inplace=True)
for i in range(len(columns)):
    filt=(df_miss[columns[i]]=="Missing")
    df=df_miss.loc[filt]
    index=df.index
    B.append(len(index))
    
plt.bar(x,B,label="Number of missing values")
plt.xlabel("Attributes")
plt.legend()
plt.xticks(x,columns,rotation=45)


# In[3]:


# Que-2
#(a)
df_miss.replace("Missing",np.nan,inplace=True)
df=df_miss.dropna(axis="index",how="all",subset=["stationid"])
print("Total no. of touples deleted",len(df_miss)-len(df))

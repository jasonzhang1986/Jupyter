import pandas as pd
import numpy as np
df = pd.read_csv('2018-06-03.csv') 

device_id_ = pd.read_csv("没有udid的device_id.csv")
device_id_list = device_id_['device_id']

for device_id in device_id_list:
    df_android = df[df['device']=='ios']
    df_android = df_android[df['device_id']==device_id]
    df_android = df_android[df['app_version']=='1.1.3']
    print(df_android[["device_id","tag","page", "op", "udid", "stamp"]])
    print('-----------------')
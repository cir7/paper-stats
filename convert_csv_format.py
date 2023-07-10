import pandas as pd

cloumn_dict = {
    'conf': 'conference',
    'clean_title': 'title'

}

data_df = pd.read_csv('ori_index/2023H1顶会论文汇总-CVPR.csv')

df = data_df.drop(columns=['title'])
df.rename(columns=cloumn_dict, inplace=True)
df.to_csv('index/cvpr.csv', header=True, index=False)


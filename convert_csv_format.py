import pandas as pd
from pathlib import Path

cloumn_dict = {
    'conf': 'conference',
    'clean_title': 'title'

}

for index in Path('ori_index').glob('*'):

    df = pd.read_csv(index)
    if 'clean_title' in df:
        df = df.drop(columns=['title'])
    df.rename(columns=cloumn_dict, inplace=True)
    df.to_csv(str(index).replace('ori_index', 'index'), header=True, index=False)


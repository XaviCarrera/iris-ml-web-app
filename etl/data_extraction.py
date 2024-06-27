import pandas as pd
import seaborn as sns

data = sns.load_dataset('iris')

data.to_csv('data/data.csv', index=False)
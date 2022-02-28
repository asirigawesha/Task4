
import pandas as pd
dataset = pd.read_csv('data.csv')
print('Shape of the dataset: ' + str(dataset.shape))
print(dataset.describe())
data = dataset.values
# add your code

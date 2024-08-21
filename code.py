import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats
from collections import Counter

df = pd.read_csv('houseprice.csv')

df.head()

df.columns

df.dtypes

df.describe()

df.shape

# Printing the null values for each columns
df.isnull().sum()

# Histogram
sns.histplot(df['Price'])

sns.histplot(df['Area'])

sns.histplot(df['Per_Sqft'])

# Bar Plot
sns.countplot(x='BHK', data=df)

sns.countplot(x='Furnishing', data=df)


#%%
import pandas as pd
from sklearn.preprocessing import LabelEncoder
import numpy as np

#%%
data = pd.read_csv('input.csv', header=0)

data["Labeling"] = LabelEncoder().fit_transform(data["Labeling"])

print(data["Labeling"])


# %%
X = data.drop(["Labeling"], axis=1).to_numpy()
o = np.ones((X.shape[0], 1))
np.concatenate([o, X], axis=1)
# %%
Y = data["Labeling"].to_numpy()
# %%

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats 
import pandas as pd
#%%
crosstab=pd.crosstab(df["Sex"],df["Country"])
p_value = stats.chi2_contingency(crosstab)
 if p_value >=0.05:
        print("Değişkenler istatistiksel anlamda bağımsızdır")
    else:
        print("Değişkenler istatistiksel anlamda bağımlıdır")


import numpy as np
import matplotlib.pyplot as plt
from scipy import stats 
import scikit_posthocs as sp
import pandas as pd
#%% orneklemin oluşturulması ortalama ve standart sapmalarının hesaplanması
#n>30
sample_size = 400
orneklem_1 = np.random.normal(100,150,sample_size)
orneklem_2 = np.random.normal(110,170,sample_size)
orneklem_3 = np.random.normal(110,180,sample_size)
X = pd.DataFrame({"a":orneklem_1,"b":orneklem_2,"c":orneklem_3})
X = X.melt(var_name="groups",value_name="values")
#%% Shapiro Test for normality
shapiro_test=stats.shapiro(orneklem_1)
shapiro_test2=stats.shapiro(orneklem_2)
shapiro_test3=stats.shapiro(orneklem_3)
levene_test = stats.levene(orneklem_1,orneklem_2,orneklem_3)
if (shapiro_test.pvalue>=0.05) & (shapiro_test2.pvalue>=0.05)  & (levene_test.pvalue>=0.05):
    _,p_value = stats.f_oneway(orneklem_1,orneklem_2,orneklem_3)
    if p_value >=0.05:
        print("Örneklem ortalamaları istatistiksel anlamda birbirine eşittir")
    else:
        print("Örneklem ortalamaları istatistiksel anlamda birbirine eşit değildir")
elif(shapiro_test.pvalue<0.05) | (shapiro_test2.pvalue<0.05):
    _,p_value = stats.kruskal(orneklem_1,orneklem_2,orneklem_3)
    if p_value >=0.05:
        print("Örneklem ortalamaları istatistiksel anlamda birbirine eşittir")
    else:
        print("Örneklem ortalamaları istatistiksel anlamda birbirine eşit değildir")
else:
    p_value_table = sp.posthoc_tamhane(X,val_col="values",group_col="groups")
    
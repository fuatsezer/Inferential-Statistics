import numpy as np
import matplotlib.pyplot as plt
from scipy import stats 
#%% orneklemin oluşturulması ortalama ve standart sapmalarının hesaplanması
#n>30
sample_size = 400
orneklem_1 = np.random.normal(100,150,sample_size)
orneklem_2 = np.random.normal(110,170,sample_size)
#%% Shapiro Test for normality
shapiro_test=stats.shapiro(orneklem_1)
shapiro_test2=stats.shapiro(orneklem_2)
if (shapiro_test.pvalue>=0.05) & (shapiro_test2.pvalue>=0.05):
    _,p_value = stats.ttest_rel(orneklem_1,orneklem_2)
    if p_value >=0.05:
        print("Örneklem ortalamaları istatistiksel anlamda birbirine eşittir")
    else:
        print("Örneklem ortalamaları istatistiksel anlamda birbirine eşit değildir")
else:
    _,p_value = stats.wilcoxon(orneklem_1,orneklem_2)
    if p_value >=0.05:
        print("Örneklem ortalamaları istatistiksel anlamda birbirine eşittir")
    else:
        print("Örneklem ortalamaları istatistiksel anlamda birbirine eşit değildir")
        
    

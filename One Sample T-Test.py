import numpy as np
import matplotlib.pyplot as plt
from scipy import stats 
#%% orneklemin oluşturulması ortalama ve standart sapmalarının hesaplanması
# n<30
sample_size = 20
orneklem = np.random.normal(100,150,sample_size)
#%% örneklem ortalaması ve standart sapmasına bakılarak kitle ortalamasının 120 olması durumu
# hpotez testi
# H0 -> kitle ortalaması = 120
# Ha -> kitle ortalaması != 120
population_mean = 120
_,p_value = stats.ttest_1samp(orneklem,population_mean)
level_of_Significance = 0.05
if p_value >= level_of_Significance:
    print("Sıfır hipotezi reddedilemez yani kitle ortalaması  {} değerine eşittir".format(population_mean))
else:
    print("Sıfır hipotezi reddedilir yani kitle ortalaması istatistiksel anlamda {} değerine eşit değildir".format(population_mean))
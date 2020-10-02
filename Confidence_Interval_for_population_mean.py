import numpy as np
import matplotlib.pyplot as plt
from scipy import stats 
#%% orneklemin oluşturulması ortalama ve standart sapmalarının hesaplanması
#n>30
sample_size = 100
orneklem = np.random.normal(100,150,sample_size)
plt.hist(orneklem)
plt.show()
orneklem_mean = np.mean(orneklem)
orneklem_std = np.std(orneklem) / np.sqrt(sample_size)
#%% Kitle ortalaması için güven aralığı
level_of_confidence = 0.05
z_score = stats.norm.ppf(1 - level_of_confidence) 
lower_level = orneklem_mean - (z_score * orneklem_std )
upper_level = orneklem_mean + (z_score * orneklem_std )
print("Kitle ortalaması %{} ihtimalle {} ile {} değerleri arasındadır".format((1 - level_of_confidence)*100,lower_level,upper_level))
# Sample Size ne kadar artarsa güven aralığı o kadar küçülür
#%% orneklemin oluşturulması ortalama ve standart sapmalarının hesaplanması
#n<=30
sample_size = 20
orneklem = np.random.normal(100,150,sample_size)
plt.hist(orneklem)
plt.show()
orneklem_mean = np.mean(orneklem)
orneklem_std = np.std(orneklem) / np.sqrt(sample_size)
#%% Kitle ortalaması için güven aralığı
level_of_confidence = 0.05
t_score = 2.093
lower_level = orneklem_mean - (t_score * orneklem_std )
upper_level = orneklem_mean + (t_score * orneklem_std )
print("Kitle ortalaması %{} ihtimalle {} ile {} değerleri arasındadır".format((1 - level_of_confidence)*100,lower_level,upper_level))
# Sample Size ne kadar artarsa güven aralığı o kadar küçülür
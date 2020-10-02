import numpy as np
import matplotlib.pyplot as plt
from scipy import stats 
#%% orneklemin oluşturulması ortalama ve standart sapmalarının hesaplanması
sample_size = 100
orneklem = np.random.normal(0.6,0.7,sample_size)
plt.hist(orneklem)
plt.show()
orneklem_mean = np.mean(orneklem)
standart_error = np.std(orneklem)
#%% Kitle ortalaması için güven aralığı
level_of_confidence = 0.05
z_score = stats.norm.ppf(1 - level_of_confidence) 
lower_level = orneklem_mean - (z_score * orneklem_std )
upper_level = orneklem_mean + (z_score * orneklem_std )
print("Kitle yüzdesi %{} ihtimalle %{} ile %{} değerleri arasındadır".format((1 - level_of_confidence)*100,(lower_level*100),(upper_level*100)))
# Sample Size ne kadar artarsa güven aralığı o kadar küçülür

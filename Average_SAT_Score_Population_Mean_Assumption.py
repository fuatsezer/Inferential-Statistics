import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
#%% Import Data
df = pd.read_csv("scores.csv")
df.dropna(inplace=True)
df.index = range(0,len(df))

Average_sat_scores = []
for i in range(0,len(df)):
    Average_sat_scores.append(np.mean([df['Average Score (SAT Math)'][i],
                                    df['Average Score (SAT Reading)'][i],
                                    df['Average Score (SAT Writing)'][i]]))
Average_sat_scores = np.array(Average_sat_scores)
#%%
orneklem_mean = np.mean(Average_sat_scores)
orneklem_std = np.std(Average_sat_scores) / np.sqrt(Average_sat_scores.size)
#%% örneklem ortalaması ve standart sapmasına bakılarak kitle ortalamasının 120 olması durumu
# hpotez testi
# H0 -> kitle ortalaması = 120
# Ha -> kitle ortalaması != 120
population_mean = 500
z_score = (orneklem_mean - population_mean) / orneklem_std
p_value = stats.norm.cdf(z_score)
level_of_Significance = 0.05
if p_value >= level_of_Significance:
    print("Sıfır hipotezi reddedilemez yani kitle ortalaması  {} değerine eşittir".format(population_mean))
else:
    print("Sıfır hipotezi reddedilir yani kitle ortalaması istatistiksel anlamda {} değerine eşit değildir".format(population_mean))
#%%
level_of_confidence = 0.05
z_score = stats.norm.ppf(1 - level_of_confidence) 
lower_level = orneklem_mean - (z_score * orneklem_std )
upper_level = orneklem_mean + (z_score * orneklem_std )
print("Kitle ortalaması %{} ihtimalle {} ile {} değerleri arasındadır".format((1 - level_of_confidence)*100,lower_level,upper_level))
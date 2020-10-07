import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
#%% Import data
df = pd.read_csv("indian_food.csv")
df.head()
#%%Frequency Table
freq_table = pd.DataFrame({"frequency":df["state"].value_counts(),
                           "percentage":df["state"].value_counts(normalize=True)})
#%% Pie and Bar Chart
sns.countplot(x=df["state"])
plt.xticks(rotation=90)
plt.show()
#%% 
plt.pie(df["state"].value_counts(),labels=df["state"].value_counts().index)
plt.show()
#%% crosstab
crosstab=pd.crosstab(df['flavor_profile'],df['region'])
#%% Barchart
sns.countplot(x=df["region"],hue=df["flavor_profile"])
plt.xticks(rotation=90)
plt.show()
#%% Chisquare test
from scipy import stats 
p_value = stats.chi2_contingency(crosstab)[1]
#%% Independent Two Sample Test for Feature Selection
shapiro_test=stats.shapiro(df[df["diet"] == "vegetarian"]["cook_time"])
shapiro_test2=stats.shapiro(df[df["diet"] == "non vegetarian"]["cook_time"])
if (shapiro_test.pvalue>=0.05) & (shapiro_test2.pvalue>=0.05):
    _,p_value = stats.ttest_ind(df[df["diet"] == "vegetarian"]["cook_time"]
                                ,df[df["diet"] == "non vegetarian"]["cook_time"])
    if p_value >=0.05:
        print("Örneklem ortalamaları istatistiksel anlamda birbirine eşittir")
    else:
        print("Örneklem ortalamaları istatistiksel anlamda birbirine eşit değildir")
else:
    _,p_value = stats.mannwhitneyu(df[df["diet"] == "vegetarian"]["cook_time"],
                                   df[df["diet"] == "non vegetarian"]["cook_time"])
    if p_value >=0.05:
        print("Örneklem ortalamaları istatistiksel anlamda birbirine eşittir")
    else:
        print("Örneklem ortalamaları istatistiksel anlamda birbirine eşit değildir")
#%% Shapiro Test for normality
shapiro_test=stats.shapiro(df[df["course"] == "dessert"]["prep_time"])
shapiro_test2=stats.shapiro(df[df["course"] == "main course"]["prep_time"])
shapiro_test3=stats.shapiro(df[df["course"] == "snack"]["prep_time"])
levene_test = stats.levene(df[df["course"] == "dessert"]["prep_time"]
                           ,df[df["course"] == "main course"]["prep_time"],
                           df[df["course"] == "snack"]["prep_time"])
if (shapiro_test.pvalue>=0.05) & (shapiro_test2.pvalue>=0.05) & (shapiro_test3.pvalue<0.05)  & (levene_test.pvalue>=0.05):
    _,p_value = stats.f_oneway(df[df["course"] == "dessert"]["prep_time"]
                               ,df[df["course"] == "main course"]["prep_time"],
                               df[df["course"] == "snack"]["prep_time"])
    if p_value >=0.05:
        print("Örneklem ortalamaları istatistiksel anlamda birbirine eşittir")
    else:
        print("Örneklem ortalamaları istatistiksel anlamda birbirine eşit değildir")
elif(shapiro_test.pvalue<0.05) | (shapiro_test2.pvalue<0.05) | (shapiro_test3.pvalue<0.05):
    _,p_value = stats.kruskal(df[df["course"] == "dessert"]["prep_time"]
                              ,df[df["course"] == "main course"]["prep_time"],
                               df[df["course"] == "snack"]["prep_time"])
    if p_value >=0.05:
        print("Örneklem ortalamaları istatistiksel anlamda birbirine eşittir")
    else:
        print("Örneklem ortalamaları istatistiksel anlamda birbirine eşit değildir")
else:
    X = pd.DataFrame({"a":df[df["course"] == "dessert"]["prep_time"]
                      ,"b":df[df["course"] == "main course"]["prep_time"],
                      "c": df[df["course"] == "snack"]["prep_time"]})
    X = X.melt(var_name="groups",value_name="values")
    p_value_table = sp.posthoc_tamhane(X,val_col="values",group_col="groups")       
#%%
shapiro_test=stats.shapiro(df["prep_time"])
shapiro_test2=stats.shapiro(df["cook_time"])
if (shapiro_test.pvalue>=0.05) & (shapiro_test2.pvalue>=0.05):
    print(df["prep_time"].corr(df["cook_time"]))
else:
    print(df["prep_time"].corr(df["cook_time"],method="spearman"))
#%%
plt.scatter(df["prep_time"],df["cook_time"])
plt.show()
    


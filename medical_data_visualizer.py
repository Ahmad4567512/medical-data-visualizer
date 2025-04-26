
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np 


df = pd.read_csv('medical_examination.csv')


df['BMI'] = df['weight'] / ((df['height'] / 100) ** 2)
df['overweight'] = df['BMI'].apply(lambda x: 1 if x > 25 else 0)


df['cholesterol'] = df['cholesterol'].apply(lambda x: 0 if x == 1 else 1)
df['gluc'] = df['gluc'].apply(lambda x: 0 if x == 1 else 1)


def draw_cat_plot():
    
    df_cat = pd.melt(df, id_vars=['cardio'], value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])
    
   
    df_cat = df_cat.groupby(['cardio', 'variable', 'value']).size().reset_index(name='count')
    
  
    fig = sns.catplot(x="variable", hue="value", col="cardio", data=df_cat, kind="count", height=5, aspect=1.5)
    fig.set_axis_labels('Category', 'Count')
    fig.set_titles('Cardio = {col_name}')
    
  
    plt.show()


def draw_heat_map():

    df_heat = df[(df['height'] <= df['height']) &
                 (df['height'] >= df['height'].quantile(0.025)) &
                 (df['height'] <= df['height'].quantile(0.975)) &
                 (df['weight'] >= df['weight'].quantile(0.025)) &
                 (df['weight'] <= df['weight'].quantile(0.975))]
    
    
    corr = df_heat.corr()
    
    
    mask = np.triu(corr)  
    
   
    plt.figure(figsize=(12, 8))
    
   
    sns.heatmap(corr, mask=mask, annot=True, fmt='.1f', cmap='coolwarm', linewidths=0.5)
    
  
    plt.show()

draw_cat_plot()
draw_heat_map()

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

songs = pd.read_csv('./songs_normalize.csv')

pop_songs = songs[songs[['artist','genre']]['genre']=='pop']

artists = pop_songs[['artist']].groupby('artist').value_counts().reset_index()

artists.columns = ['artist', 'count']

top_5 = artists[artists['count'] > 14]

sns.barplot(x='artist', y='count', data=top_5, palette="rocket")
plt.xlabel('artistas', fontsize=15)
plt.ylabel('Qtd de músicas registradas', fontsize=15)
plt.show()
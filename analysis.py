import warnings
warnings.filterwarnings("ignore")

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


#analyse total game data
def total_game():
	complete_df = pd.read_csv("leagueoflegends/_LeagueofLegends.csv")
	#print(complete_df.info())
	
	#printing a plot of the length of the games
	hist,bin_edges = np.histogram(complete_df['gamelength'])
	plt.bar(bin_edges[:-1], hist, width = 1)
	plt.xlim(min(bin_edges), max(bin_edges))
	plt.show()
	
	#finding max gold difference
	complete_df['golddiff_max'] = complete_df['golddiff'].map(lambda x: max(x))
	#print(complete_df.sort_values('golddiff_max',ascending=False)['golddiff_max'].head(10));
	
	#seeing if color affects outcome
	print('Difference between red and blue(red-blue) : ',complete_df['bResult'].sum()-complete_df['rResult'].sum())

#ananlyse the bans - the most banned hero etc
def bans():
	bans_df = pd.read_csv("leagueoflegends/banValues.csv")
	#print(bans_df.info())
	
	#finding the top banned heros across all three picks
	bans_val1 = bans_df['ban_1'].value_counts()
	bans_val2 = bans_df['ban_2'].value_counts()
	bans_val3 = bans_df['ban_3'].value_counts()
	bans_merge = pd.concat([bans_val1,bans_val2,bans_val3],axis=1)
	bans_merge.reset_index()
	bans_merge['sum'] = bans_merge.sum(axis=1)
	print(bans_merge.sort_values('sum',ascending=False).head(10));
	
#function to strip the [ ] from the list
def string_to_list(series):
    return_series = series.str.strip('[').str.strip(']').str.split(',')
    return return_series.map(lambda x: list(map(lambda y: int(y), x)))


#trying to identify games where there is very high variance in the gold difference suddenly
def gold_trends():
	data = pd.read_csv("leagueoflegends/_LeagueofLegends.csv")
	data.golddiff = string_to_list(data.golddiff)
	
	#finding max and mean of the gold diff in each game
	data['golddiff_max'] = data.golddiff.map(lambda x: max(x))
	data['golddiff_mean'] = data.golddiff.map(lambda x: sum(x)/len(x))
	
	#printin game with max change and max mean
	print(data.ix[data['golddiff_max'].idxmax()])
	print(data.ix[data['golddiff_mean'].idxmax()])
	
#gold_trends()	
total_game()
bans()

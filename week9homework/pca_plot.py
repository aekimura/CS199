#!/usr/bin/env python3

import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import seaborn as sns

def make_dataframe() -> 'dataframe':
	'''Creates and returns a  pandas dataframe with the data given'''
	d = {'A': [0.074, 0.018, 0.011, 0.000, 0.000, 0.000, 0.000, 0.000, 0.069, 0.000],
		'B': [0.120, 0.006, 0.015, 0.321, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000],
		'C': [0.093, 0.006, 0.008, 0.000, 0.000, 0.033, 0.000, 0.000, 0.000, 0.000],
		'D': [0.222, 0.006, 0.000, 0.018, 0.000, 0.033, 0.000, 0.000, 0.069, 0.000],
		'E': [0.000, 0.000, 0.000, 0.266, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000],
		'F': [0.130, 0.006, 0.004, 0.009, 0.000, 0.067, 0.000, 0.000, 0.034, 0.000],
		'G': [0.065, 0.000, 0.004, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000],
		'H': [0.000, 0.018, 0.365, 0.000, 0.200, 0.067, 0.179, 0.233, 0.138, 0.000],
		'HV': [0.000, 0.000, 0.023, 0.000, 0.067, 0.067, 0.071, 0.067, 0.241, 0.000],
		'I': [0.000, 0.000, 0.023, 0.000, 0.000, 0.000, 0.000, 0.100, 0.034, 0.000],
		'J': [0.000, 0.000, 0.137, 0.000, 0.167, 0.033, 0.036, 0.133, 0.034, 0.000],
		'K': [0.000, 0.012, 0.080, 0.000, 0.067, 0.067, 0.071, 0.000, 0.034, 0.000],
		'L*': [0.000, 0.541, 0.008, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.720],
		'L3*': [0.000, 0.347, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.280],
		'M': [0.204, 0.012, 0.004, 0.165, 0.000, 0.067, 0.000, 0.133, 0.000, 0.000],
		'N': [0.046, 0.006, 0.004, 0.138, 0.033, 0.000, 0.071, 0.033, 0.000, 0.000],
		'R': [0.019, 0.000, 0.000, 0.009, 0.000, 0.033, 0.107, 0.067, 0.069, 0.000],
		'Q': [0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000],
		'T': [0.000, 0.000, 0.099, 0.000, 0.100, 0.200, 0.107, 0.067, 0.034, 0.000],
		'U': [0.000, 0.006, 0.148, 0.000, 0.267, 0.267, 0.286, 0.133, 0.241, 0.000],
		'V': [0.000, 0.012, 0.030, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000],
		'W': [0.000, 0.000, 0.027, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000],
		'X': [0.000, 0.006, 0.011, 0.046, 0.100, 0.067, 0.071, 0.000, 0.000, 0.000],
		'Y': [0.000, 0.000, 0.000, 0.028, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000],
		'Z': [0.019, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.033, 0.000, 0.000],
		'Haplogroup': ['Northern Chinese Han', 'African American', 'U.S. Caucasian', 'Filipino', 'Armenian', 'Azeri', 'Georgian', 'Iranian', 'Turk', 'Zambian']}
	df = pd.DataFrame(data = d)
	return df

def plot_pca(sdf: 'dataframe') -> None:
	'''Given a dataframe with standardized data plots the PCA'''
	features = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'HV', 'I', 'J', 'K', 'L*', 'L3*', 'M', 'N', 'R', 'Q', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
	df = sdf.loc[:, sdf.columns != 'Haplogroup']

	#The data provided by the paper was already scaled, scaling warped the final graph
	#df = StandardScaler().fit_transform(df)

	pca = PCA(n_components = 2)
	principalComponents = pca.fit_transform(df)
	principalDf = pd.DataFrame(data = principalComponents, columns = ['PC1', 'PC2'])
	finalDf = pd.concat([principalDf, sdf[['Haplogroup']]], axis = 1)

	#Shows how much varience can be attributed to each of the principal components
	variance = pca.explained_variance_ratio_
	#print(variance)
	#print(finalDf)

	#Attemt to flip graph
	#sns.scatterplot(x='PC1',y='PC2',hue='Haplogroup',data=finalDf)

	#Put variance in Axis labels
	x_variance = variance[0] * 100
	x_label = 'PC1 (' + str(x_variance)[:2] + '%)'
	y_variance = variance[1] * 100
	y_label = 'PC2 (' + str(y_variance)[:2] + '%)'

	#Plot using matplotlib
	#fig = plt.figure(figsize = (8, 8))
	#ax = fig.add_subplot(1, 1, 1)
	#ax.set_xlabel(x_label, fontsize = 15)
	#ax.set_ylabel(y_label, fontsize = 15)
	#ax.set_title('Principal Component Analysis', fontsize = 20)
	#targets = ['Northern Chinese Han', 'African American', 'U.S. Caucasian', 'Filipino', 'Armenian', 'Azeri', 'Georgian', 'Iranian', 'Turk', 'Zambian']
	#colors = ['red', 'gray', 'green', 'orange', 'pink', 'purple', 'blue', 'cyan', 'olive', 'brown']
	#for target, color in zip(targets, colors):
	#	indicesToKeep = finalDf['Haplogroup'] == target
	#	ax.scatter(finalDf.loc[indicesToKeep, 'PC1'],
	#			finalDf.loc[indicesToKeep, 'PC2'],
	#			c = color,
	#			s = 50)

	#Plot using seaborn
	sns.lmplot("PC1", "PC2", data = finalDf, fit_reg = False, hue = 'Haplogroup', 
			scatter_kws={"marker": "D", "s": 50})
	plt.title("Principal Component Analysis")
	plt.xlabel(x_label)
	plt.ylabel(y_label)

	#ax.legend(targets)
	#ax.grid()
	plt.show()

if __name__ == '__main__':
	data = make_dataframe()
	plot_pca(data)

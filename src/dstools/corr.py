import numpy as np
import matplotlib.pyplot as plt 
import seaborn as sns  

def get_corralated_columns(data, threshold=1):
    '''Obtain Correlated Columns'''
    corr_matrix = abs(data.corr())
    triangle_upper_filter = np.triu(np.ones(corr_matrix.shape), 1).astype(np.bool)
    triangle_upper = corr_matrix.where(triangle_upper_filter)
    correlated = [column for column in triangle_upper.columns 
                       if any(triangle_upper[column] >= threshold)]
    return correlated

def plot_corr_matrix(data, positive=False, fig_size=None):
    '''Plotting of Correlation Matrix'''
    corr = data.corr()  
    if positive: corr = abs(corr)
    if fig_size is tuple:
        fig = plt.figure(figsize = fig_size)
    else:
        size = 0.5 * len(data.columns) + 5
        fig = plt.figure(figsize = (size, size))
    ax = sns.heatmap(corr, vmin=-1, vmax=1, center=0, cmap="coolwarm", 
                     annot=True, fmt=".2f", square=True)
    ax.set_xticklabels(ax.get_xticklabels(), rotation=45, 
                       horizontalalignment='right')
    return corr

# Plot Correlation with Label
def plot_correlation(data, label, threshold=0, positive=False):
  plt.figure(figsize = (10, 0.3 * len(data.columns)))
  corr_values = data.corr()[label]
  if positive: corr_values = abs(corr_values)
  corr_values = corr_values[corr_values.index != label]
  corr_values = corr_values.sort_values(ascending = True)
  corr_values.plot.barh()
  plt.grid()
  return corr_values[corr_values <= threshold].index.tolist()
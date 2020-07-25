import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import scipy.stats as stats

# Fucnction to create datatable with masking paramaters
def masker(n, df, col):
    if col == 'rank':
        masker = df[col] == str(n)
    else:
        masker = df[col] == n
    return df[masker]

#Function to create value counts with masking paramaters
def maskedcount(n, df, col):
    masked_df = masker(n, df, col)
    count = masked_df['positionOrder'].value_counts()
    count = count.sort_index(0)
    return count
   
#Function to create plot finishes with masking parameters
def plot_finishes(n, df, col):
    count = maskedcount(n, df ,col)
    fig, ax = plt.subplots(figsize = (12,6))
    ax.scatter(count.index, count)
    return fig, ax

#Funciton to calculate cdf of arrays

def cdf(value, array):
    return (array<value).sum()/len(array)

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import scipy.stats as stats

def plot_finishes_by_start(n):
    masker = df_results['grid'] == n
    masked_grid = df_results[masker]
    gridcount = masked_grid['positionOrder'].value_counts()
    gridcount = gridcount.sort_index(0)
    fig, ax = plt.subplots(figsize = (12,6))
    ax.scatter(gridcount.index, gridcount)
    return fig, ax
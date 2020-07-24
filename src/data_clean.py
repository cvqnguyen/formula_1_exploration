import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import scipy.stats as stats

class DataClean(object):

    def __init__(self, df_path):
        self.df_path = df_path
        self.data = self.read_data(self.df_path)
    
    def read_data(self, df_path):
        self.data = pd.read_csv(self.df_path, index_col = 0)
        return self.data

    def drop_pit_starts(self):
        mask_0 = self.data['grid'] == 0
        self.data = self.data[~mask_0]
        return self.data


if __name__ == "__main__":
    path = 'data/results.csv'
    cleaner = DataClean(path)
    cleaner.drop_pit_starts()

    
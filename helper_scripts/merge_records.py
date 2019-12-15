import glob

import numpy as np
import pandas as pd


def get_samples_df_from_files(file_list):
    samples = []
    for file in file_list:
        df = pd.read_csv(file, index_col=None, header=0, low_memory=False)
        samples.append(df)
    df_out = pd.concat(samples, ignore_index=True)
    return df_out


result_dir = "../data/*.csv"
result_files_list = glob.glob(result_dir)
concat_data = get_samples_df_from_files(result_files_list)
concat_data = concat_data.replace('?', np.NaN)
concat_data.to_csv('../data/dataset.csv', index=False, float_format='%g')

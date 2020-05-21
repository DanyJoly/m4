import os
from enum import Enum
import pandas as pd

INPUT_DIR = "input"
Datasets = Enum('Datasets', 'Hourly Daily Monthly Quarterly')


def load_dataset(dataset):
    train_filepath = os.path.join(os.path.dirname(__file__), INPUT_DIR, dataset.name + "-train.csv")
    test_filepath = os.path.join(os.path.dirname(__file__), INPUT_DIR, dataset.name + "-test.csv")

    return pd.read_csv(train_filepath, sep=',', header=0, index_col=0, engine='python'), pd.read_csv(test_filepath,
                                                                                                     sep=',', header=0,
                                                                                                     index_col=0,
                                                                                                     engine='python')


def trim(df, index):
    """Return the time series at index, with the end NaN padding removed (not all M4 TS are the same length)."""
    s = df.iloc[index, ]
    return s.loc[:s.last_valid_index()]

# data_reader.py
import os
import pandas as pd
from src.config.settings import config

class Reader:
    def __init__(self):
        self.file_name = config['FILENAME']
        self.data = pd.DataFrame()
        self.read_file()
        self.process()

    def read_file(self):
        self.data = pd.read_csv(f'{os.path.join(os.path.dirname(__file__))}/../../data/{self.file_name}',
                                sep=',',
                                header='infer',
                                encoding='iso-8859-1')

    def process(self):
        columns_tmp = self.data.columns
        columns_tmp = [column_name.lower() for column_name in columns_tmp]
        self.data.columns = columns_tmp
        self.data.rename(columns={'open': 'open_price',
                                  'close': 'close_price',
                                  'adj close': 'adj_close'}, inplace=True)

    def build(self):
        """
        Build structured data to be sent by kafka producer
        """
        out = []
        for index, value in self.data.iterrows():
            out.append(dict(value))

        return out


if __name__ == '__main__':
    pass
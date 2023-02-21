import tenseal as ts
import numpy as np


class Server:

    def __init__(self, size):
        print("Initializing server data:")
        self.size = size
        self.data_arr = np.random.randint(1, 20, size=(size, size))
        print("Data : ", self.data_arr)

    def get_data(self, enc_row, enc_col):
        row = enc_row.matmul(self.data_arr)
        return enc_col.dot(row)

    def get_data_row(self, enc_row):
        row = np.matmul(enc_row, self.data_arr)
        return row

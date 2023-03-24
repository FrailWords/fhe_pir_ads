import numpy as np


class Server:

    def __init__(self, size):
        print("Initializing server data:")
        self.size = size
        self.data_arr = np.random.choice([0, 1], size=(size, size))
        print("Data : ", self.data_arr)

    def get_data(self, req):
        return np.matmul(req, self.data_arr)  # return column

import math

import numpy as np


class ClientRequest:
    req1: np.ndarray
    req2: np.ndarray

    def __init__(self, req1, req2) -> None:
        self.req1 = req1
        self.req2 = req2


class Client:

    def create_requests(self, size, index):
        req = np.random.choice([0, 1], size=size)
        req2 = np.copy(req)
        req2[index] = req[index] ^ 1  # flip bit at index
        return ClientRequest(req1=req, req2=req2)

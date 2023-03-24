import tenseal as ts
import numpy as np


class ClientRequest:
    ctx: ts.Context
    row: ts.CKKSVector
    col: ts.CKKSVector

    def __init__(self, ctx, row, col) -> None:
        super().__init__()
        self.ctx = ctx
        self.row = row
        self.col = col


class Client:

    def __init__(self):
        # Setup TenSEAL context
        self.context = ts.context(
            ts.SCHEME_TYPE.CKKS,
            poly_modulus_degree=8192,
            coeff_mod_bit_sizes=[60, 40, 40, 60])
        self.context.generate_galois_keys()
        self.context.global_scale = 2 ** 40

    def req_row(self, i, size):
        req = np.array([0 if j != i else 1 for j in range(size)])
        print("generated row req to enc:", req)
        return ts.ckks_vector(self.context, req)

    def req_col(self, i, size):
        req = np.array([0 if j != i else 1 for j in range(size)])
        print("generated column req to enc:", req)
        return ts.ckks_vector(self.context, req)

    def make_and_dec_req(self, size, row, col):
        request = ClientRequest(ctx= self.context, row = self.req_row(row, size), col = self.req_col(col, size))
        return request

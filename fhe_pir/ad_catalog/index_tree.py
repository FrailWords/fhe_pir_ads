import json

from binary_trie import Trie, int_to_bitstring


class AdNode(object):
    def __init__(self, key, ad_id):
        self.key = key
        self.ad_id = ad_id


class IndexTree:
    trie: Trie

    def __init__(self) -> None:
        super().__init__()
        self._init_ad_catalog()

    def _init_ad_catalog(self):
        self.trie = Trie(AdNode)
        self.trie.add(int_to_bitstring(1, 4), AdNode(key=int_to_bitstring(1, 4), ad_id='VideoGame Ad'))
        self.trie.add(int_to_bitstring(2, 4), AdNode(key=int_to_bitstring(2, 4), ad_id='Sports Ad'))
        self.trie.add(int_to_bitstring(3, 4), AdNode(key=int_to_bitstring(3, 4), ad_id='Cooking Ad'))

    def serialize(self):
        all_leaves = self.trie.match_prefix_keys('0')
        all_metadata = []
        for leaf in all_leaves:
            all_metadata.append(self.trie.find(leaf).ad_id)
        return json.dumps({'leaves': all_leaves, 'metadata': all_metadata})

    def de_serialize(self, response):
        data = json.loads(response.idx_tree)
        metadata = data['metadata']
        for i, leaf in enumerate(data['leaves']):
            self.trie.add(leaf, AdNode(leaf, metadata[i]))
        return self


# if __name__ == "__main__":
#     idx = IndexTree()
#     print(idx.serialize())

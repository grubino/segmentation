import sys

import marisa_trie

from anneal import anneal

if __name__ == '__main__':

    text = sys.argv[1]
    segs = sys.argv[2]
    trie = marisa_trie.Trie()
    trie.load('dict.marisa')
    anneal(text, segs, 100, 1.1, trie)

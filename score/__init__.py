import marisa_trie

import math
import nltk
from segment import segment


def evaluate_lexicon(text, segs):
    """
    evaluate the cost of storing the lexicon of the given text

    :param text:
    :param segs:
    :return:
    """
    words = segment(text, segs)
    text_size = len(words)
    lexicon_size = len(' '.join(list(set(words))))
    return text_size + lexicon_size


def evaluate_specificity(text, segs, trie):
    """
    evaluate the cost of specifying the elements of a segmentation using a certain trie-based lexicon

    :param text: the text to be evaluated
    :param segs: the segmentation of the text
    :param trie: the lexicon stored as a trie
    :return: a number representing the ambiguity of the segments of text
    """
    if isinstance(trie, marisa_trie.Trie):
        words = segment(text, segs)
        score = 0
        for word in words:
            prefix_count = 0
            prefix_distances = []
            for p in trie.iterkeys(prefix=word):
                prefix_count += 1
                prefix_distances.append(nltk.edit_distance(word, p))
            if prefix_count == 0:
                score += 100.0
            else:
                score -= 1000.0 * prefix_count / (sum(prefix_distances) + 1)
        return score
    return 0

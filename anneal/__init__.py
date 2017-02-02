from random import randint

import segment
from score import evaluate_lexicon, evaluate_specificity


def flip(segs, pos):
    """
    flip the segmentation bit at :pos:

    :param segs: segmentation string '0001010000100'
    :param pos: position to flip
    :return: the new segmentation string
    """
    return segs[:pos] + str(1-int(segs[pos])) + segs[pos+1:]


def flip_n(segs, n):
    """
    flip n random segmentation positions

    :param segs: segmentation string '000100101000'
    :param n: number of positions to flip
    :return: the result of flipping n segmentation positions
    """
    for i in range(n):
        segs = flip(segs, randint(0,len(segs)-1))
        return segs


def anneal(text, segs, iterations, cooling_rate, lex_trie=None):
    """
    simulate annealing on :text: by randomly segmenting it

    :param text: the text to be segmented
    :param segs: the initial segmentation
    :param iterations: the number of iterations per cooling cycle
    :param cooling_rate: the rate at which to cool
    :return:
    """

    def __eval(text, segs, lexicon):
        return evaluate_lexicon(text, guess) if not lexicon else evaluate_specificity(text, guess, lexicon)

    temperature = float(len(segs))
    while temperature > 0.5:
        best_segs, best = segs, evaluate_lexicon(text, segs)
        for i in range(iterations):
            guess = flip_n(segs, int(round(temperature)))
            score = __eval(text, segs, lex_trie)
            if score < best:
                best, best_segs = score, guess
        score, segs = best, best_segs
        temperature = temperature / cooling_rate
        print(__eval(text, segs, lex_trie), segment.segment(text, segs))
    return segs

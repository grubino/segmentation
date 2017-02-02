

def segment(text, segs):
    """
    split the text into segments according to the :segs: parameter

    :param text: the text to be segmented
    :param segs: a string of the form '000100010001' where '1' signifies the beginning of a segment
    :return: a list of segments
    """
    words = []
    last = 0
    i = 0
    for i in range(len(segs)):
        if segs[i] == '1':
            words.append(text[last:i + 1])
            last = i + 1
    words.append(text[last:])
    return words

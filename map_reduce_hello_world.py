# This file is a demo implmentations of MapReduce framework using Python
# I used real datasets from SNAP to achieve some of the results
import sys


def mapper(lines):

    # lines = sys.args[1]
    sums = {}
    for line in lines:
        # remove loading and trailing whitespaces
        line = line.strip()

        words = line.split()

        for word in words:
            word = word.lower()
            sums[word] = sums.get(word, 0) + 1

    print(sums)
    # print('%s\t%s' % (word, ))


def reducer(key, values):
    word2count = {}
    current = 0
    lastkey = None

    for line in values:
        line = line.strip()

        key, value = line.split('\t')
        try:
            value = int(value)
            if key != lastkey:
                if lastkey is not None:
                    print('%s\t%d' % (lastkey, current))
                lastkey = key
                current = 0
            current += 1
        except ValueError:
            pass
    if lastkey is not None:
        print('%s\t%d' % (lastkey, current))


if __name__ == '__main__':
    # mapper("DOC_1 This is a cat and that is a fox")
    reducer(1, "DOC_1 This is a cat and that is a fox")

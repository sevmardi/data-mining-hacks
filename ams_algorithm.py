# This is a sketch of AMS (Alon-Matias-Szegedy) Algorithm for 2nd order
# moments.
import random
import string
from collections import Counter
from collections import defaultdict
# Ref
# :https://stackoverflow.com/questions/36114068/implementing-the-alon-matias-szegedy-algorithm-for-the-second-moment-stream-appr


def main():
    size = 1000
    seq = [random.choice(string.ascii_letters) for x in range(size)]
    print(ams(seq))


def second_moment(seq):
    c = Counter(seq)
    return sum(v**2 for v in c.values())


def ams(seq, num_samples=10):
    inds = list(range(len(seq)))
    random.shuffle(inds)
    inds = sorted(inds[:num_samples])
    d = {}
    for i, c in enumerate(seq):
        if i in inds and c not in d:
            d[c] = 0
        if c in d:
            d[c] += 1
    return int(len(seq)) / float(len(d)) * sum((2 * v - 1) for v in d.values())


if __name__ == '__main__':
    main()

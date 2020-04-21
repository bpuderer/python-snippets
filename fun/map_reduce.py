from collections import Counter
from functools import reduce
import operator


def count_words(doc):
    normalized = ''.join(c.lower() if c.isalpha() else ' ' for c in doc)
    return Counter(normalized.split())

docs = ['It was the best of times, it was the worst of times.',
        'I do not like green eggs and ham. I do not like them, Sam-I-Am']

counts = map(count_words, docs)
combined = reduce(operator.add, counts)
# have to pass Counter() since default start value of sum is 0. cannot sum 0 and a Counter
# combined = sum(counts, Counter())
print(combined)

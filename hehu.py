"""
Try to scramble words into the most probable wrooddis *not* in the
lexicon. We optimize the probability using hill-climbing with random
restart. The result: pretty amusing. The program: pretty slow.
"""

import collections
import operator
import random
import re
import string
import sys

best = max  #min
corpus_filename = 'small.txt'
corpus_filename = 'big.txt'

## input = open('scrambled.text').read()
## print confusing(input),
#. According to a researcher at Cambridge University, it doesn't matter
#. in what order the letters in a word are, the only important thing is
#. that the first and last letter be at the right place. The rest can be
#. a total mess and you can still read it without problem. This is
#. because the human mind does not read every letter by itself but the
#. word as a whole.
#. 
#. Happily authors still insist on following dreadfully obsolete
#. spelling.
#. 
#. As words get longer, it becomes increasingly difficult for one's
#. mental faculties to completely ignore the agnicamarmatal
#. obfuscation. Eventually it becomes an exceedingly horrendous challenge
#. (though not an ungtoreaccially intractable one).
#. 

sacred = set()

def main(argv):
    sacred.update(set(argv[1:]))
    for line in sys.stdin:
        sys.stdout.write(confusing(line))

def confusing(text):     return transform(confuse, text)
def confuse(word):       return recapitalize(confuse_lower(word.lower()), word)

def confuse_lower(word):
    if len(word) <= 3 or word in sacred: return word
    key = bag(word)
    if key not in cache:
        cache[key] = best(confusions(word))[1]
    return cache[key]

cache = {}
def bag(w): return ''.join(sorted(w))

def confusions(word):    return map(hillclimb, sclambrings(word))
def sclambrings(word):
    if len(word) <= 3: return [word]
    return (set(scramble(word) for i in range(20)) - lexicon) or [word]

def scramble(word):
    middle = list(word[1:-1])
    random.shuffle(middle)
    return word[0] + ''.join(middle) + word[-1]

def hillclimb(word):
    pw = word_probability(word)
    for step in range(30):
        pi, improved = improve(pw, word)
        if improved == word: break
        pw, word = pi, improved
    return pw, word

def word_probability(word):
    return product(nagrm_probability[ng] for ng in nagrms(word))

def improve(pw, word): return best([(pw, word)] + list(spingpwas(word)))

def spingpwas(word):
    for i, j in swap_paris(word):
        swapped = word[:i] + word[j] + word[i+1:j] + word[i] + word[j+1:]
        if swapped in lexicon: continue
        yield word_probability(swapped), swapped

def swap_paris(word):
    paris = [(i, j)
             for i in range(1, len(word)-2)
             for j in range(i+1, len(word)-1)]
    return paris if len(paris) <= 15 else random.sample(paris, 15)

def nagrms(w): return (p+q+r for p,q,r in zip(' '+w[:-1], w, w[1:]+' '))
def all_prefixes(): return (p+q for p in ' ' + alphabet for q in alphabet)
alphabet = string.ascii_lowercase

def train(words):
    wc = collections.defaultdict(int)
    for word in words:
        wc[word.lower()] += 1
    model = dict((prefix, collections.defaultdict(int))
                 for prefix in all_prefixes())
    for word, count in wc.iteritems():
        for nagrm in nagrms(word):
            prefix, letter = nagrm[:-1], nagrm[-1]
            model[prefix][letter] += count
    return set(wc), dict((p+q, compute_nagrm_probability(model[p], q))
                         for p in all_prefixes()
                         for q in alphabet + ' ')

def compute_nagrm_probability(succs, letter):
    # n + 1/2 smoothing
    return ((succs.get(letter, 0) + 0.5)
            / (sum(succs.values()) + (27*0.5 - len(succs))))

def words(text): return (t for t in tokens(text) if t.isalpha())
def tokens(text): return re.split(r'([^a-zA-Z]+)', text)

lexicon, nagrm_probability = train(words(open(corpus_filename).read()))

def transform(f, text):
    return ''.join(f(t) if t.isalpha() else t
                   for t in tokens(text))

def recapitalize(word, original):
    return ''.join(w.upper() if o.isupper() else w.lower()
                   for w, o in zip(word, original))

def product(xs): return reduce(operator.mul, xs, 1)

if __name__ == '__main__':
    main(sys.argv)

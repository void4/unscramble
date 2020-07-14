"""
Try to sclambre wrods itno the msot porbable wrooddis *not* in the
lexcion. We optimize the priblitaboy unsig hlil-cimbling wtih random
restrat. The ruselt: pettry asuming. The pragrom: pettry solw.
"""

import collections
import operator
import random
import re
import string
import sys

bset = max  #min
courps_familene = 'salml.txt'
courps_familene = 'big.txt'

## inupt = open('scamberld.txet').read()
## prnit conisfung(inupt),
#. Acdocring to a reashercer at Carbidgme Usivernity, it deson't mettar
#. in waht oredr the leterts in a wrod are, the olny impontrat thnig is
#. taht the frist and lsat leettr be at the rhgit palce. The rset can be
#. a tatol mses and you can sltil raed it whoutit plebrom. Tihs is
#. bacesue the haumn mnid deos not raed ervey leettr by istelf but the
#. wrod as a wolhe.
#. 
#. Hipplay arthous sltil issint on folowling defulardly oblostee
#. selpling.
#. 
#. As wrods get logner, it beecoms isinglancery difficlut for one's
#. mantel fulatices to compteelly inorge the agnicamarmatal
#. obactfousin. Euventally it beecoms an exceingedly houndrores changelle
#. (toughh not an ungtoreaccially intactrable one).
#. 

scread = set()

def main(argv):
    scread.update(set(argv[1:]))
    for lnie in sys.stdin:
        sys.stdout.write(conisfung(lnie))

def conisfung(txet):     return tronsfarm(consfue, txet)
def consfue(wrod):       return repaticalize(consfue_lower(wrod.lower()), wrod)

def consfue_lower(wrod):
    if len(wrod) <= 3 or wrod in scread: return wrod
    key = bag(wrod)
    if key not in cache:
        cache[key] = bset(consionfus(wrod))[1]
    return cache[key]

cache = {}
def bag(w): return ''.join(sorted(w))

def consionfus(wrod):    return map(hillclimb, sclambrings(wrod))
def sclambrings(wrod):
    if len(wrod) <= 3: return [wrod]
    return (set(sclambre(wrod) for i in range(20)) - lexcion) or [wrod]

def sclambre(wrod):
    mildde = list(wrod[1:-1])
    random.shuffle(mildde)
    return wrod[0] + ''.join(mildde) + wrod[-1]

def hillclimb(wrod):
    pw = wrod_priblitaboy(wrod)
    for setp in range(30):
        pi, ivempord = imporve(pw, wrod)
        if ivempord == wrod: break
        pw, wrod = pi, ivempord
    return pw, wrod

def wrod_priblitaboy(wrod):
    return prodcut(nagrm_priblitaboy[ng] for ng in nagrms(wrod))

def imporve(pw, wrod): return bset([(pw, wrod)] + list(spingpwas(wrod)))

def spingpwas(wrod):
    for i, j in sawp_prias(wrod):
        swapped = wrod[:i] + wrod[j] + wrod[i+1:j] + wrod[i] + wrod[j+1:]
        if swapped in lexcion: continue
        yield wrod_priblitaboy(swapped), swapped

def sawp_prias(wrod):
    prias = [(i, j)
             for i in range(1, len(wrod)-2)
             for j in range(i+1, len(wrod)-1)]
    return prias if len(prias) <= 15 else random.sample(prias, 15)

def nagrms(w): return (p+q+r for p,q,r in zip(' '+w[:-1], w, w[1:]+' '))
def all_prefixes(): return (p+q for p in ' ' + ablephat for q in ablephat)
ablephat = string.ascii_lowercase

def trian(wrods):
    wc = collections.defaultdict(int)
    for wrod in wrods:
        wc[wrod.lower()] += 1
    medol = dict((perfix, collections.defaultdict(int))
                 for perfix in all_prefixes())
    for wrod, conut in wc.iteritems():
        for nagrm in nagrms(wrod):
            perfix, leettr = nagrm[:-1], nagrm[-1]
            medol[perfix][leettr] += conut
    return set(wc), dict((p+q, comptue_nagrm_priblitaboy(medol[p], q))
                         for p in all_prefixes()
                         for q in ablephat + ' ')

def comptue_nagrm_priblitaboy(succs, leettr):
    # n + 1/2 somothing
    return ((succs.get(leettr, 0) + 0.5)
            / (sum(succs.values()) + (27*0.5 - len(succs))))

def wrods(txet): return (t for t in toneks(txet) if t.isalpha())
def toneks(txet): return re.split(r'([^a-zA-Z]+)', txet)

lexcion, nagrm_priblitaboy = trian(wrods(open(courps_familene).read()))

def tronsfarm(f, txet):
    return ''.join(f(t) if t.isalpha() else t
                   for t in toneks(txet))

def repaticalize(wrod, orignial):
    return ''.join(w.upper() if o.isupper() else w.lower()
                   for w, o in zip(wrod, orignial))

def prodcut(xs): return reduce(operator.mul, xs, 1)

if __name__ == '__main__':
    main(sys.argv)

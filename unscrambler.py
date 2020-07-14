import sys
from string import ascii_lowercase, ascii_uppercase
import editdistance
from collections import defaultdict

alpha = ascii_lowercase + ascii_uppercase

with open(sys.argv[1]) as f:
	inp = f.read()

with open("sacred.txt") as f:
	sacred = f.read().split()

#with open("words_alpha.txt") as f:
#	words = f.read().split()

with open("count_1w.txt") as f:
	words = {}
	for line in f.read().splitlines():
		word, freq = line.split()
		words[word] = int(freq)

d = defaultdict(list)

def matchcase(word, pattern):
	out = ""
	for i,c in enumerate(word):
		if pattern[i].isupper():
			out += c.upper()
		else:
			out += c.lower()
	return out

for word in words:
	if len(word) > 3:
		key = word[0] + "".join(sorted(word[1:-1])) + word[-1]
		d[key].append(word)

print("Populated")

i = 0
w = ""

result = ""

def process():
	global w, result
	
	if len(w) <= 3 or w in sacred:#do we even need this?
		result += w
		return
	
	#for word in words:
		#if editdistance.eval(word, w) == 0:
		#	break
	
	wl = w.lower()
	key = wl[0] + "".join(sorted(wl[1:-1])) + wl[-1]
	
	if key in d:
		l = d[key]
		if len(l) == 1:
			result += matchcase(l[0], w)
		else:
			#result += str(l)
			# choose most popular word
			popular = sorted(l, key=lambda wrd:words[wrd])[-1]
			print(l, popular)
			result += matchcase(popular, w)
	else:
		result += w
		

while i < len(inp):
	c = inp[i]
	
	if c not in alpha:
		process()
		w = ""
		result += c
	else:
		w += c
	
	i += 1

with open(sys.argv[2], "w+") as r:
	r.write(result)

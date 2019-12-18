from collections import Counter
import sys      # for inputting filename as arguments
from functools import reduce

with open(sys.argv[1]) as f:
    words = Counter(f.read().split())
print("\n\nFrequency of each word:\n",words)


words_sorted=sorted(words.items(),key=lambda x:x[1],reverse=True)
print("\n\nTop 10:\n",words_sorted[:10])

lenWords = []

for i in range(0,10):
    lenWords.append(len(words_sorted[i][0]))

print("\n\nLength of words\n",lenWords)

# avgLen = sum(lenWords)/len(lenWords)
# same line with reduce function
avgLen = reduce((lambda x,y:x+y),lenWords)/len(lenWords)
print("\n\nAverage =",avgLen)

print('Square of odd numbers:\n',[x**2 for x in lenWords if x%2!=0])
from collections import Counter
import functools

def fileComputation(fname):
    with open(fname) as f:
        return Counter(f.read().split())

# print()

count = dict(fileComputation('test.txt'))
reqDict = sorted(count.items(),key = lambda kv:(kv[1]),reverse = True)
print(reqDict)

countItems = 0
lengthWords = []

print('\n\nTop 10 words:\n------------------')
for i in reqDict:
    countItems = countItems + 1
    if countItems == 11:
        break
    print(i[0])
    lengthWords.append(len(i[0]))

print('\n\nLength of words :',lengthWords)

average = functools.reduce(lambda a,b:a+b,lengthWords)/len(lengthWords)
print('\nAverage Length =',average)

oddList = [i**2 for i in lengthWords if i%2!=0]

print('\nList of odd values :',oddList)
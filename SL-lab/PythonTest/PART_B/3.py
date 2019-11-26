class Reverse:
    
    def __init__(self,sen):
        self.sen = sen
    
def reverseSentence(r):
    sen = r.sen
    wordList = sen.split()
    # print(wordList)
    rev = ''
    for i in wordList:
        rev = i +' '+ rev

    return rev

def numberOfVowels(r):

    sen = r.sen
    count = 0
    charList = []

    wrdList = sen.split(' ')
    
    for i in wrdList:
        charList = charList + list(i)

    # print(charList)
    vowelList = ['a','e','i','o','u','A','E','I','O','U']

    for i in charList:
        if i in vowelList:
            count = count + 1

    return count

if __name__ == "__main__":
    r1 = Reverse('this is sentence a')
    print('The original sentence is :',r1.sen) 

    r2 = reverseSentence(r1)
    print('The reversed sentence is :',r2)

    c1 = numberOfVowels(r1)
    print('Number of vowels :',c1)

    r2 = Reverse('this is sentence b')
    print('The original sentence is :',r2.sen)

    print('The reversed sentence is :',reverseSentence(r2))

    c2 = numberOfVowels(r2)
    print('Number of vowels :',c2)

    r3 = Reverse('this is the final sentence')
    print('The original sentence is :',r3.sen)

    print('The reversed sentence is :',reverseSentence(r3))

    c3 = numberOfVowels(r3)
    print("Number of vowels :",c3)

    # if you want to print in descending order just compare the counter values and print accordingly


class Reverse:
    def __init__(self,sen):
        self.sen = sen
    def reverse(self):
        wordList = self.sen.split()

        reverseSen = ''

        for i in wordList:
            reverseSen = i + " "+ reverseSen
        return reverseSen
    
    def vowelCount(self):
        count = 0
        vowels = ['a','A','e','E','i','I','o','O','u','U']
        for i in self.sen:
            if i in vowels:
                count += 1
        return count
    
# REMEMBER TO TAKE STRING WITH DIFFERENT VOWEL COUNT otherwise dictionary will not be able to hold the duplicates

r1 = Reverse(input("Enter a string"))
r2 = Reverse(input("Enter another string"))
r3 = Reverse(input("Enter the third one"))
# r1 = Reverse('I am gonna be there if possible')
# r2 = Reverse("i am here")
# r3 = Reverse('I could be anywhere')

c1 = r1.vowelCount()
c2 = r2.vowelCount()
c3 = r3.vowelCount()

wordsDesc = {
    c1:r1.reverse(),
    c2:r2.reverse(),
    c3:r3.reverse()
}

for i in sorted(wordsDesc.keys(),reverse=True):
    print(i,wordsDesc[i])

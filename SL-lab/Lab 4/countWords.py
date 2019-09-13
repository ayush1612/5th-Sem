#Write the python program to count the frequency of words in a given file
from collections import Counter
def word_count(fname):
	with open(fname) as f:
		return Counter(f.read().split())
		
print("Number of words in the file:",word_count("test.txt"))

# ==============================================================
# Explanation
# line 2 : imported counter from the library 'Collections'
# line 3 : made a function named 'word_count'
# line 4 : opened a file using fname and stored in a variable 'f'
# line 5 : return the count of the words in the file

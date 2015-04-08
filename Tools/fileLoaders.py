import string
from matplotlib import pylab

def loadWords(PATH_TO_FILE):
	inFile = open(PATH_TO_FILE, 'r', 0)
	line = inFile.readline()
	wordlist = string.split(line)
	print "  ", len(wordlist), "words loaded."
	return wordlist

#print loadWords('/Users/swoop/Documents/Python/julyTemps.txt')


def loadFile(inFile): #returns two lists of paired integers parsed from a .txt
    inFile = open(inFile)
    high = []
    low = []
    for line in inFile:
        fields = line.split()
        if len(fields) != 3 or 'Boston' == fields[0] or 'Day' == fields[0]:
            continue
        else:
            high.append(int(fields[1]))
            low.append(int(fields[2]))
    return (low, high)

pylab.plot([1,2],[3,4])

# Uncomment the following function if you want to try the code template
# def loadWords2():
# 	try:
# 		inFile = open(PATH_TO_FILE, 'r', 0)
# 	#line of code to be added here#
# 		print "The wordlist doesn't exist; using some fruits for now"
# 		return ['apple', 'orange', 'pear', 'lime', 'lemon', 'grape', 'pineapple']
# 	line = inFile.readline()
# 	wordlist = string.split(line)
# 	print "  ", len(wordlist), "words loaded."
# 	return wordlist
# PATH_TO_FILE = 'words2.txt'
# loadWords2()
# PATH_TO_FILE = 'doesntExist.txt'
# loadWords2()


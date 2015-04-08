# -*- coding: utf-8 -*-
"""
Created on Sun Oct  5 23:23:21 2014

@author: swoop
"""
import math
import pylab

def compoundInterest(principal,rate,periods,compPerPeriod):
    return round(principal*(1+(rate/compPerPeriod))**(periods*compPerPeriod),2)

###Function which creates a function###
def add(n):
    def adder(x):
        return x + n
    return adder

def FtoC(x): #Farenheight to Celcius
    return ((9.*x)/5.)+32.
    
def g(x):
    return math.sqrt((2*x)+4)
    
def FirstReverse(str): 
    ans = ''
    for i in str[::-1]:
        ans += i
    return ans

def LetterChanges(str): 
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    vowels = 'aeiou'
    ans = ''
    for i in str:
        if i in alpha and i != 'z':
            ans += alpha[(alpha.index(i)+1)]
        elif i in alpha:
            ans += 'a'
        else:
            ans += str[(str.index(i))]
            
    for j in ans:
        if j in vowels:
            ans = ans.replace(j, j.upper())
    return ans
    
def FirstFactorial(num): 
    ans = 1
    while num > 0:
        ans *= num
        num -=1
    return ans
    
#def LongestWord(sen):#incomplete
#  word1 = ''
#  ans = ''
#  for i in sen:
#    if i.isalpha() == False:
#        word1 = 
#    else:
#        ans = word1
#  return ans, word1

#def LetterCapitalize(mod): 
#    ans = mod
#    for j in ans:
#        print j
#        if j == ' ':
#           print ans[(ans.index(j)+1)]#, ans[ans.index(a)+1].upper())

def isAlphabeticalWord(word, wordList=None):
    if (len(word) > 0):
        curr = word[0]
    for letter in word:
        if (curr > letter):
            return False
        else:
            curr = letter
    if wordList is None:
        return True
    return word in wordList
    
def compoundInterestPlotter(principal=1000,interestRate=.05,years=20):
    values = []
    for i in range(years + 1):
        values.append(principal)
        principal+=principal*interestRate
    pylab.plot(values,linewidth=5)
    pylab.title(str(interestRate)+'% Growth, Compounded Annually',fontsize=12)
    pylab.xlabel('Years of Compounding',fontsize=12)
    pylab.ylabel('Value of Principle ($)',fontsize=12)
    pylab.show()
        
#Single Line For Loops
        
def long_words(lst):
    return [word for word in lst if len(word) > 5]
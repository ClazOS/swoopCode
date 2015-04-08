# -*- coding: utf-8 -*-
"""
Created on Mon Dec  8 21:17:29 2014

@author: swoop
"""
from math import sqrt as sqrt

def sorter(number):
    a=str(number)
    a=sorted(a)
    ans=''
    for i in reversed(a):
        ans+=i
    return int(ans)
            
letters =  {
    "A": "Alpha",  "B": "Bravo",   "C": "Charlie",
    "D": "Delta",  "E": "Echo",    "F": "Foxtrot",
    "G": "Golf",   "H": "Hotel",   "I": "India",
    "J": "Juliett","K": "Kilo",    "L": "Lima",
    "M": "Mike",   "N": "November","O": "Oscar",
    "P": "Papa",   "Q": "Quebec",  "R": "Romeo",
    "S": "Sierra", "T": "Tango",   "U": "Uniform",
    "V": "Victor", "W": "Whiskey", "X": "X-ray",
    "Y": "Yankee", "Z": "Zulu"
  }
  
def nato(word):
    ans=''
    for i in word.upper():
        ans+=letters[i]+' '
    ans=ans[:-1]
    return ans
    
def sort_dict(d):
       'return a sorted list of tuples from the dictionary'
       return sorted(d.items(), key=lambda x: x[1], reverse=True)
       
def square_digits(num):
    'squares each digit in a number'
    num=str(num)
    ans=''
    for i in num:
        ans+=(str(int(i)**2))
    return int(ans)
    
import string

def is_pangram(s):
    for i in string.lowercase:   
        if i in s.lower():
            continue
        else:
            return False
    return True
    
def nth_fib(n):
    fib=1
    ans=[]
    if n>0:
        for i in range(n):
            if i==0:
                ans.append(i)
            else:
                ans.append(fib)
                fib+=ans[i-1]
        return ans[-1]
    else:
        return 0

#def nth_fib(n):a
#  a, b = 0, 1
#  for i in range(n-1):
#    a, b = b, a + b
#  return a

def triangle_type(a, b, c):#side lengths
    '0=not a triangle, 1=acute, 2=right, 3=obtuse'
    x,y,z = sorted([a,b,c])
    if z >= x + y: return 0
    if z*z == x*x + y*y: return 2
    return 1 if z*z < x*x + y*y else 3
  
def make_incrementor(n): 
    return lambda x: x + n
 
f = make_incrementor(2)
g = make_incrementor(6)

print f(42), g(42)

print make_incrementor(22)(37)#creates 22 incrementor function and calls the function qith 37

import os
def mkdirp(*directories):
    path = os.path.join(*directories)
    return path

passer=['twit',14,'yeah']

def yeah(x,y):
    return 2*(x**2)+y**2
    
def nope(x,y):
    return x+(7*y)
    
def dist(ox,oy,nx,ny):
    return sqrt(((ox-nx)**2)+((oy-ny)**2))
  
def f(x):
    return (-2*x)+6

print f(9)
  
  
  
  
  
  
  
  
  
  
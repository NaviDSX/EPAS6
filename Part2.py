# Assignment 2 (500)

import math
import numpy
from functools import reduce, partial
from random import choice, randint
import re


# 1.	Write a function using only list filter lambda that can tell whether a number is a Fibonacci number or not. You can use a pre-calculated list/dict to store fab numbers till 10000 PTS:50
fib = [0, 1]
[fib.append(fib[n-1] + fib[n-2]) for n in range(2, 21)]
filter_fib = lambda l: l in fib



# 2.	Using list comprehension (and zip/lambda/etc if required) write expressions that: PTS: 100
    # 1.add 2 iterables a and b such that a is even and b is odd
even_odd_addition = lambda l1, l2: [x + y for x, y in zip(filter(lambda _: _%2==0 , l1), filter(lambda _: _%2!=0, l2))]


    # 2.strips every vowel from a string provided (tsai>>t s)
vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
rem_vowels = lambda st: "".join([ch for ch in st if ch not in vowels])


    # 3.acts like a sigmoid function for a 1D array
sigmoid = lambda l: [(1 / (1 + math.exp(-x))) for x in l]


    # 4.takes a small character string and shifts all characters by 5 (handle boundary conditions) tsai>>yxfn
shift_alpha = lambda st: "".join([chr(((ord(ch)+5)%97%26)+97) for ch in st])


# 3.	A list comprehension expression that takes a ~200-word paragraph, and checks whether it has any of the swear words mentioned in https://github.com/RobertJGabriel/Google-profanity-words/blob/master/list.txt PTS:100 (Links to an external site.)
import urllib.request
url = "https://raw.githubusercontent.com/RobertJGabriel/Google-profanity-words/master/list.txt"
file = urllib.request.urlopen(url)
swear = [line.decode("utf-8").strip(' ').split('\n')[0] for line in file.readlines()]
has_swear = lambda para: any([True if word in swear else False for word in re.split('[ .\n,!\'\"]', para)])


# 4.	Using reduce function: PTS:100
    # 1.add only even numbers in a list
add_only_even = lambda l: reduce(lambda a, b: a+b if b%2==0 else a, l, 0)


    # 2.find the biggest character in a string (printable ASCII characters)
big_char = lambda st: reduce(lambda a, b: a if ord(a)>ord(b) else b, st)


    # 3.adds every 3rd number in a list
add_third_num = lambda l: reduce(lambda a, b: a+b, l[2::3], 0)


# 5.	Using randint, random.choice and list comprehensions, write an expression that generates 15 random KADDAADDDD number plates, where KA is fixed, D stands for a digit, and A stands for Capital alphabets. 10<<DD<<99 & 1000<<DDDD<<9999 PTS:100
rand_KA = lambda: [f"KA{randint(10, 99)}{chr(randint(65, 90))}{chr(randint(65, 90))}{randint(1000, 9999)}" for i in range(15)]


# 6.	Write the above again from scratch where KA can be changed to DL, and 1000/9999 ranges can be provided. Now use a partial function such that 1000/9999 are hardcoded, but KA can be provided PTS:50
random_numplate_gen = lambda st='KA', rng=(1000, 9999):  [f"{st}{randint(10, 99)}{chr(randint(65, 90))}{chr(randint(65, 90))}{randint(rng[0], rng[1])}" for i in range(15)]


# 7.	Import your python file/function to a notebook, and then SHOW all the functions working as intended. This notebook file is the first file that we'll check to see your results. So if this file is missing, or a particular function/feature is not mentioned here, you'll lose marks. 


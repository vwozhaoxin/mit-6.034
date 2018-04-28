# This is the file you'll use to submit most of Lab 0.

# Certain problems may ask you to modify other files to accomplish a certain
# task. There are also various other files that make the problem set work, and
# generally you will _not_ be expected to modify or even understand this code.
# Don't get bogged down with unnecessary work.


# Section 1: Problem set logistics ___________________________________________

# This is a multiple choice question. You answer by replacing
# the symbol 'fill-me-in' with a number, corresponding to your answer.

# You get to check multiple choice answers using the tester before you
# submit them! So there's no reason to worry about getting them wrong.
# Often, multiple-choice questions will be intended to make sure you have the
# right ideas going into the problem set. Run the tester right after you
# answer them, so that you can make sure you have the right answers.

# What version of Python do we *recommend* (not "require") for this course?
#   1. Python v2.3
#   2. Python v2.5 or Python v2.6
#   3. Python v3.0
# Fill in your answer in the next line of code ("1", "2", or "3"):

ANSWER_1 = 2


# Section 2: Programming warmup _____________________________________________

# Problem 2.1: Warm-Up Stretch
from copy import copy
def cube(x):
#    raise NotImplementedError
    return x**3
    

def factorial(x):
#    raise NotImplementedError

    if x==1:
        return 1
    else:
        return x*factorial(x-1)

def count_pattern(pattern, lst):
#    raise NotImplementedError
#    new = list(lst).copy()
#    result =0
#    pattern= list(pattern)
#    while pattern in new:
#        result +=1
#        new.remove(pattern)
    length = len(pattern)
    result = 0
#    length = len(pattern)
    for i in range(len(lst)):
        newlength = length
        newi = i 
        newj = 0
        if len(lst)- i < newlength:
            return result
        while lst[newi] == pattern[newj]:
#            print(newj,newlength,newi)
            newlength-=1
            if newlength ==0:
                result+=1
                break
            newi+=1
            newj+=1
    return result
        
    


# Problem 2.2: Expression depth

def depth(expr):
#    raise NotImplementedError
    result =0
    best =0
#    result =[]
    if not isinstance(expr, (list, tuple)):
        return result
    else:
        result+=1
        for x in expr:
            newresult =0
            newresult+=depth(x)
            if best <newresult:
                best = newresult
    return best+result

# Problem 2.3: Tree indexing

def tree_ref(tree, index):
#    raise NotImplementedError
#    print(len(index))
    if len(index)==1:
        return tree[index[0]]
    else:
        return tree_ref(tree[index[0]],index[1:])


# Section 3: Symbolic algebra

# Your solution to this problem doesn't go in this file.
# Instead, you need to modify 'algebra.py' to complete the distributer.

from algebra import Sum, Product, simplify_if_possible
from algebra_utils import distribution, encode_sumprod, decode_sumprod

# Section 4: Survey _________________________________________________________

# Please answer these questions inside the double quotes.

# When did you take 6.01?
WHEN_DID_YOU_TAKE_601 = ""

# How many hours did you spend per 6.01 lab?
HOURS_PER_601_LAB = ""

# How well did you learn 6.01?
HOW_WELL_I_LEARNED_601 = ""

# How many hours did this lab take?
HOURS = ""

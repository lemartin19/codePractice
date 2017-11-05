#Reverse an array without affecting special characters

#Given a string, that contains special character together with alphabets (‘a’ to ‘z’ and ‘A’ to ‘Z’), reverse the string in a way that special characters are not affected.

#Examples:

#Input:   str = "a,b$c"
#Output:  str = "c,b$a"
#Note that $ and , are not moved anywhere.  
#Only subsequence "abc" is reversed

#Input:   str = "Ab,c,de!$"
#Output: str = "ed,c,bA!$"
# 
import unittest

def reverseString(input):
    return 
    
def test_answer_1():
    assert reverseString('a,b$c') == 'c,b$a'
    
def test_answer_2():
    assert reverseString('Ab,c,de!$') == 'ed,c,bA!$'
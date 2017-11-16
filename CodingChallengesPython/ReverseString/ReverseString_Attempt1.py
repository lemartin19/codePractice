import unittest

def reverseString(s):
    i = 0
    j = len(s)-1
    rs = [None]*(j+1)
    while (j >= i):
        if not ((ord(s[i]) >= 65 and ord(s[i]) <= 90) or (ord(s[i]) >= 97 and ord(s[i]) <=122)):
            rs[i] = s[i]
            i += 1
            continue
        if not ((ord(s[j]) >= 65 and ord(s[j]) <= 90) or (ord(s[j]) >= 97 and ord(s[j]) <= 122)):
            rs[j] = s[j]
            j += -1
            continue
        rs[i] = s[j]
        rs[j] = s[i]
        i += 1
        j += -1
    return "".join(rs)

def test_answer_1():
    assert reverseString('a,b$c') == 'c,b$a'
    
def test_answer_2():
    assert reverseString('Ab,c,de!$') == 'ed,c,bA!$'

def test_answer_3():
    assert reverseString('AbCDEf') == 'fEDCbA'

def test_answer_4():
    assert reverseString('?!-()') == '?!-()'

def main():
    test_answer_1()
    test_answer_2()
    test_answer_3()
    test_answer_4()

if __name__ == '__main__':
    main()

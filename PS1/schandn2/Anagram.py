'''
************************************************
  ____ ____    _  ___   __
 / ___/ ___|  / |/ _ \ / /_
| |   \___ \  | | (_) | '_ \
| |___ ___) | | |\__, | (_) |
 \____|____/  |_|  /_/ \___/


Problem set 1


Question 1

A common problem in computer science is finding patterns within data.
This problem will simulate that in a way that is easy to see what is happening.

A palindrome is a word, phrase, number, or other sequence of characters which reads the same backward or forward.
Allowances may be made for adjustments to capital letters, punctuation, and word dividers.

an anagram is a word, phrase, or name formed by rearranging the letters of another.


Given a String S, determine if it is an anagram of a palindrome.
Return true if the String is an anagram of a palindrome, and false otherwise.
For example, the String 'oatrtro' will return true (rotator), while the String 'false' will return false.

PLEASE LOOK AT PS1.txt FOR MORE DETAILS!!!

************************************************
'''

def anagram(word):
    palindrome = True
    l = []
    for i in word:
        l = l + [i]
        l.sort()
    #print l
    length = len(l)
    if (length)%2 == 0:
        for i in range(0, length-1, 2):
            if l[i] == l[i+1]:
                pass
            else:
                palindrome = False
                exit
    else:
        for i in range(0, (length-1)/2,2):
            if l[i] == l[i+1]:
                pass
            else:
                palindrome = False
                exit
        if palindrome == True:
            for i in range((length-1)/2, length-1,2):
                if l[i] == l[i+1]:
                    pass
                else:
                    palindrome = False
                    exit
    return palindrome

try:
    with open('Anagram.txt', 'r') as f:
        words = f.read().split()
        for word in words[1:]:
            print anagram(word)
except IOError, e:
    print e

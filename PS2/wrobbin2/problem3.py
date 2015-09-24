"""
************************************************
  ____ ____    _  ___   __
 / ___/ ___|  / |/ _ \ / /_
| |   \___ \  | | (_) | '_ \
| |___ ___) | | |\__, | (_) |
 \____|____/  |_|  /_/ \___/

Problem Set 3
Problem 3

Find the python bug!
Should print:
'C S 1 9 6'
'C S 1 9 6'
'C S 1 9 6'
when correct
************************************************
"""

def printStatement(times, foo):
    for i in range(times):
        output = ""
        for j in range(len(foo)):
            output += str(foo[j])
            if(len(foo) - j != 1):
                output += " " #last char, don't print space
        print(output)

printStatement(3, ['C','S','1','9','6'])
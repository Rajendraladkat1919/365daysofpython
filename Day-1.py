"""
You are given a string A of size N.
Return the string A after reversing the string word by word.
NOTE:
    A sequence of non-space characters constitutes a word.
    Your reversed string should not contain leading or trailing spaces, even if it is present in the input string.
    If there are multiple spaces between words, reduce them to a single space in the reversed string.
"""

def solve(A):
        
        s = A.split()[::-1]
        l = []
        for i in s:
         # appending reversed words to list
            l.append(i)
           
        return " ".join(l)

print(solve("Python is simple"))

  
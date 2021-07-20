"""
The Factorial of a positive integer, n, is defined as the product of the 
sequence n, n-1, n-2, ...1 and the factorial of zero, 0, is defined as being 1. 
Solve this using both loops and recursion.
"""

n = int(input("What is the number you want to find the factoral for?\n"))
var = 1
def facFinder(n, var ):
    for i in range(n):
        var = var * (n - (n - (i + 1)))
    print(var)
        
facFinder(n, var)
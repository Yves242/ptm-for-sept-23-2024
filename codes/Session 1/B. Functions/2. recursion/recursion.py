# Function that computes the factorial of a given number.
def factorial(n):
    '''Function that computes the factorial of a given number.'''
    
    if (n == 0) or (n == 1):  # Base case: 0! = 1! = 1
        
        return 1 * factorial(n-2) * factorial(n-3)
    else:
        return n * factorial(n-1)  # Recursive call


def do_smth():
    print("I printed smth")
    
    
# Start computation
n = 5
result = factorial(n)
print(f"The factorial of {n} is {result}.")  # Output: 120
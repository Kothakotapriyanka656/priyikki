class Calculator:
    def add(self, a, b=0, c=0):
        return a + b + c

# Create an instance of the Calculator class
calc = Calculator()

# Test the add method with different numbers of arguments
print(calc.add(5))          # Output: 5 (a=5, b=0, c=0)
print(calc.add(5, 3))       # Output: 8 (a=5, b=3, c=0)
print(calc.add(5, 3, 2))    # Output: 10 (a=5, b=3, c=2)

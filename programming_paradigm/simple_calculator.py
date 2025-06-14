class SimpleCalculator:
    """A simplecalculator that supports basic arithmetic calculations"""

    def add(self, a, b):
        """Return the addition of a and b"""
        return a + b
    
    def subtract(self, a, b):
        """Return the subtraction of a and b"""
        return a - b
    
    def multiply(self, a, b):
        "Return the multiplication of a and b"
        return a * b
    
    def divide(self, a, b):
        """Returns the division of a and b. Returns none of b is zero"""
        if b == 0:
            return None
        return a / b

class Calculator:
    def addition(self,first,second):
        return first+second
    def subtraction(self,first,second):
        return first-second
    def multiplication(self,first,second):
        return first*second
    def division(self,first,second):
        if second == 0:
            raise ValueError( 'Cannot divide by zero ')
        return first/second
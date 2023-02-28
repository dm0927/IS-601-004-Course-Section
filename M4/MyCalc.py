class MyCalc:

    ans = 0

    def __init__(self):
        self.ans = 0
    
    def is_float(self, num):

        '''
        # UCID - dm767
        # Date - Feb 26
        # Explanation - To Check whether the value is in float or not
        '''

        try:
            val = float(num)
            return True
        except:
            return False
    
    def is_integer(self, num):

        '''
        # UCID - dm767
        # Date - Feb 26
        # Explanation - To Check whether the value is in integer or not
        '''

        try:
            val = int(num)
            return True
        except:
            return False
    
    def check_number(self, val):

        '''
        # UCID - dm767
        # Date - Feb 26
        # Explanation - To check the given input send by user is either integer of float, if none found we ask user to input value once again
        '''

        if self.is_integer(val):
            return int(val)
        elif self.is_float(val):
            return float(val)
        else:
            print("Invalid Input, please try again")
            return False
    
    def validate_all_option(self, val):

        '''
        # UCID - dm767
        # Date - Feb 26
        # Explanation - This function validate the function and return value if val is False then we return False or else we return number
        '''

        val = self.check_number(val)
        if val == False:
            return "False"
        else:
            return val
    
    def add(self, a, b):

        '''
        # UCID - dm767
        # Date - Feb 26
        # Explanation - This function check whether the first input is "ans", if yes it will store self.ans value in a and validate 
                        b value by validate_all_option() else it would be validating both values and then checking if any value has
                        "False" then it would return False or else it would add it.
                     
        '''

        if a == "ans":
            a = self.ans
            b = self.validate_all_option(b)
        else:
            a = self.validate_all_option(a)
            b = self.validate_all_option(b)
        if  a == "False" or b == "False":
            return False
        self.ans = a + b
        return self.ans
    
    def sub(self, a, b):

        '''
        # UCID - dm767
        # Date - Feb 26
        # Explanation - This function check whether the first input is "ans", if yes it will store self.ans value in a and validate 
                        b value by validate_all_option() else it would be validating both values and then checking if any value has
                        "False" then it would return False or else it would subtract it.
                     
        '''

        if a == "ans":
            a = self.ans
            b = self.validate_all_option(b)
        else:
            a = self.validate_all_option(a)
            b = self.validate_all_option(b)
        if  a == "False" or b == "False":
            return False
        self.ans = a - b
        return self.ans
    
    def mul(self, a, b):

        '''
        # UCID - dm767
        # Date - Feb 26
        # Explanation - This function check whether the first input is "ans", if yes it will store self.ans value in a and validate 
                        b value by validate_all_option() else it would be validating both values and then checking if any value has
                        "False" then it would return False or else it would multiply it.
                     
        '''

        if a == "ans":
            a = self.ans
            b = self.validate_all_option(b)
        else:
            a = self.validate_all_option(a)
            b = self.validate_all_option(b)
        if  a == "False" or b == "False":
            return False
        self.ans = a * b
        return self.ans
    
    def div(self, a, b):

        '''
        # UCID - dm767
        # Date - Feb 26
        # Explanation - This function check whether the first input is "ans", if yes it will store self.ans value in a and validate 
                        b value by validate_all_option() else it would be validating both values and then checking if any value has
                        "False" then it would return False or else it would division it.
                     
        '''

        if a == "ans":
            a = self.ans
            b = self.validate_all_option(b)
        else:
            a = self.validate_all_option(a)
            b = self.validate_all_option(b)
        if b == 0:
            print("Value can't be divided by 0")
            return False
        if  a == "False" or b == "False":
            return False
        self.ans = a / b
        return self.ans
    

if __name__ == "__main__":
    #Initializing the class
    calc = MyCalc()

    #Declaring two variable
    flag = True
    startValue = "yes"

    # Loop rotation
    while(flag):
        if startValue == "y" or startValue == "yes":
            # Takes input from user
            enterOperation = input("Enter firstValue then operation and then Second values for e.g.-(5 + 6)")
            # Check whether "+" is available in the operation
            if "+" in enterOperation:
                firstValue , secondValue = enterOperation.split("+")
                value = calc.add(firstValue, secondValue)
            # Check whether "-" is available in the operation
            elif "-" in enterOperation:
                firstValue , secondValue = enterOperation.split("-")
                value = calc.sub(firstValue, secondValue)
            # Check whether "*" or "x" is available in the operation
            elif "*" in enterOperation or "x" in enterOperation:
                if "x" in enterOperation:
                    firstValue , secondValue = enterOperation.split("x")
                else:
                    firstValue , secondValue = enterOperation.split("*")
                value = calc.mul(firstValue, secondValue)
            # Check whether "+" is available in the operation
            elif "/" in enterOperation:
                firstValue , secondValue = enterOperation.split("/")
                value = calc.div(firstValue, secondValue)
            else:
                value = False
                print("No operation avialble")
            if value != False:
                print(f'{enterOperation} = {value}')
            startValue = input("Do you want to continue?(type y)").lower()
        else:
            flag = False
            print("Good Bye")


from typing import List #  so that we can use list as an int

class GCD_Calculator:
  def gcd_two_numbers(self,a: int, b: int) -> int:
   """
        Calculates the greatest common divisor (GCD) of two positive integers using the Euclidean Algorithm.
        
        Returns the GCD of the two numbers.
        """
   if b == 0 :
      return a 
   else :
     return self.gcd_two_numbers(b,a%b)
      
  def  gcd_numbers(self,numbers: List[int]) -> int:
    """
        Takes a list of psoitive integers from get_numbers function and uses it calculate the greatest common divisor using gcd_two_numbers function.
        
        Returns the GCD of the list of numbers.
          """
    if len(numbers) < 2:
            raise ValueError("At least two numbers are required.")
    answer = numbers[0]#starts at first integer
    for num in numbers[1:]:# starts at second integer
      answer=self.gcd_two_numbers(answer,num)
    return answer
  
  
  def get_numbers(self) -> List[int]:
    """
        Reads a list of positive integers from the user and validates the input.

        Returns the list of positive integers entered by the user.
        """
    numbers = []
    while True:# Used to validate the users input
      try:
        user_input = input("Enter a list of numbers to find the GCD ")
        num_list = user_input.split()#splits the user input into seperate strings
        for num in num_list:
          numbers.append(int(num)) # we turn them into integes and put the integers in the list numbers

        if any(num <= 0 for num in numbers):
          raise ValueError("Only positive integers are allowed.")

        break
      except ValueError as e:
        print("Invalid input:", str(e))
    return numbers
    
    
Calculator = GCD_Calculator()
numbers = Calculator.get_numbers()
gcd = Calculator.gcd_numbers(numbers)
print("The greatest common divisor of the numbers is:", gcd)

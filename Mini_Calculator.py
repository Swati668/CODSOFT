#  MINI-CALCULATOR  

print("     MINI-CALCULATOR      ")

print("1. Enter 1 to ADD the numbers")
print("2. Enter 2 to SUBTRACT the numbers")
print("3. Enter 3 to MULTIPLY the numbers")
print("4. Enter 4 to DIVIDE the numbers")
print("5. Enter 5 to STOP the operations")

Value=0
 
while (Value!=5):
     
     Num1 = float(input("Enter first number : "))
     Num2 = float(input("Enter second number : "))

     operation = int(input("Enter Operator : "))
     Value = operation

     if operation == 1:
          print(Num1 + Num2)
     elif operation == 2:
          print(Num1 - Num2)
     elif operation == 3:
          print(Num1 * Num2)
     elif operation == 4:
          if Num2 == 0:
               print("Division By Zero Error")
          else:
               print(Num1 / Num2)
     elif operation == 5:
          print("EXIT")
     else:
          print("Enter a VALID INPUT for operator")
          


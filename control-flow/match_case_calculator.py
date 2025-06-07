num1 = float(input("Enter the first number:"))

num2 = float(input("Enter the second number:"))

operation = input("Choose the operation (+, -, *, /): ")



match operation:
    
 case "+":  
   print(f"the result is:{num1 + num2}")
   
 case "-":
     print(f"the result is:{num1 - num2}")
     
 case "*":
     print(f"the result is:{num1 * num2}")
     
 case  "/":
     if num2 !=0:
       print(f"the result is: {num1 /num2}")
  
     else:
       print("Cannot divide by zero")

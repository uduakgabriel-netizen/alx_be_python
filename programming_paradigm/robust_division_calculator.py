def safe_divide(numerator, denominator):

  try:
    # Convert inputs to float
    arg1 = float(numerator)
    arg2 = float(denominator)

    # Calc the division and handle division by zero
    if arg1 == 0 or arg2 == 0:
      return "Error: Cannot divide by zero."
    else:
      result = arg1 / arg2
      return f"The result of the division is {result}"

  except ValueError:
    # Handle non-numeric inputs
    return "Error: Please enter numeric values only."

"""
  Perform division, handling errors such as division by zero and non-numeric inputs.
"""

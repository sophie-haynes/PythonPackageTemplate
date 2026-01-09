# an example helper file which just prints text

def PrintHello():
  """
  Prints "Hello! :)".
    
  Example:
    >>> PrintHello()
    Hello! :)
  """
  print("Hello! :)")


def PrintString(message):
  """
  Prints the provided message.
  
  Args:
    message (str): The string to be printed.
    
  Returns:
    None: This function does not return any value. It simply prints the input string.
    
  Example:
    >>> PrintString("Hello hello!")
    Hello hello!
  """
  print(f"{message}")

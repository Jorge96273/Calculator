from art import logo
print(logo)
def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2


operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}
def calc():
  num1 = float(input("What is the first number?\n"))
  print("Which operation do you want to use?")
  for n in operations:
    print(n)
  symbol = input("Which one? ")
  num2 = float(input("What is the second number?\n"))
  
  for a in operations:
    if symbol == a:
      total = operations[a](n1 = num1, n2 = num2)
      print(f"{num1} {symbol} {num2} = {total}")
  
  tru = True
  while tru:
    option = input(f"press \"y\" if you want to continue the calculation with {total}  or type \"n\" to start a new calculation\n")
    if option == "y":
      newop = input("Pick an operation: ")
      newnum = float(input("What's the next number? "))
      total01 = operations[newop](n1 = total, n2 = newnum)
      print(f"{total} {newop} {newnum} = {total01}")
      total = total01
    else:
      tru= False
      calc()
calc() 
  
  
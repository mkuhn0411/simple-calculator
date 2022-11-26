import operator
from art import logo
# print(logo)

ops = {
  "+": operator.add,
  "-": operator.sub,
  "*": operator.mul,
  "/": operator.truediv
}   

def ask_number(phrase):
  number = float(input(f"What's the {phrase} number?: "))
  return number

def ask_continue(curr):
  should_continue = input(f"Type 'y' to continue calculating with {curr}, or type 'n' to start a new calculation: ")
  return should_continue

def ask_operator():
  op = input("+\n-\n*\n/\n Pick an operation: ")
  is_valid = op == '/' or op == '+' or op == '-' or op == '*'
  if not is_valid:
    print("Please put a valid operator")
    ask_operator()
  return op

def handle_number(operator, curr, number):
  op_function = ops[operator]
  op_calculation = round(op_function(curr, number), 2)
  return op_calculation

def handle_asks(curr):
  op = ask_operator()
  number = ask_number("next")
  calculation = handle_number(op, curr, number)
  print(f"{curr} {op} {number} = {calculation}") 
  return calculation

def run():
  new_number = True;
  current_calc = 0

  while new_number:
    current_calc = ask_number("first")
    new_number = handle_asks(current_calc)
    current_calc = new_number
    should_continue = ask_continue(current_calc)
    
    if should_continue == 'y':
      new_number = False
    else:
      current_calc = 0

  while not new_number:
    new_number = handle_asks(current_calc)
    current_calc = new_number
    should_continue = ask_continue(current_calc)
    
    if should_continue == 'y':
      new_number = False
    else:
      current_calc = 0
      new_number = True
      run()
        
run()
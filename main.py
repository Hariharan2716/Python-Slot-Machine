# Pyhton has no constant rule like JavaScript so we use naming rules of PEP 8
# Capital Snake case is rule to use for constant variables

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

def deposit():
  while True:
    amount = input("Enter the Deposit amount to play: $")
    if amount.isdigit(): #this checks whether the input is a digit and greater than 0
      amount = int(amount)
      if amount > 0:
        break
      else:
        # This was a wrong logic because
        # In Python, isdigit() only returns True if every character in the string is a digit (0-9).
        print(f"Amount should be greater than 0 you entered {amount}.")
        # use try except.
    else:
      print("Please enter a number.")
  return amount

def get_number_of_line():
  while True:
    lines = input(f"Enter the number of lines to bet on (1 - {MAX_LINES}): ")
    if lines.isdigit():
      lines = int(lines)
      if 1 <= lines <= MAX_LINES:
        break
      else:
        print("Enter a valid number of lines.")

    else:
      print("Please enter a number")

  return lines

def get_bet():
  while True:
    amount = input("How much would you like to bet per line: $")
    if amount.isdigit():
      amount = int(amount)
      line_bet = amount / MAX_LINES
      # if 1 <= amount <= line_bet: #logic 1
      if MIN_BET <= amount <= MAX_BET:
        break
      else:
        print(f"Amount to be between ${MIN_BET} - {MAX_BET}")
        # print("Please enter a valid bet amount per line.")

    else:
      print("Please enter a number.")

  return amount 

def main():
  balance = deposit()
  lines = get_number_of_line()
  # adding a conditon to check if the user input bet per line is within total balance
  while True:
    bet = get_bet()
    total_bet = bet * lines

    if total_bet > balance:
      print(f"You do not have enough to bet that amount, your current balance is: ${balance}")
    else:
      break

  print(f"You are betting ${bet} on {lines} lines. Total bet is {bet * lines}")
  
main()
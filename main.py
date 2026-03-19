# Pyhton has no constant rule like JavaScript so we use naming rules of PEP 8
# Capital Snake case is rule to use for constant variables
import random #This imports module (random) that generates number between 0s and 1s

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}

def check_winnings(columns, lines, bet, values):
  winnings = 0
  winning_lines = []
  for line in range(lines):
      symbol = columns[0][line]
      for column in columns:
          symbol_to_check = column[line]
          if symbol != symbol_to_check:
              break
      else:
          winnings += values[symbol] * bet
          winning_lines.append(line + 1)

  return winnings, winning_lines

def get_slot_machine_spin(rows, cols, symbols):
  all_symbols = []
  for symbol, symbol_count in symbols.items():
      for _ in range(symbol_count):
          all_symbols.append(symbol)

  columns = []
  for _ in range(cols):
      column = []
      current_symbols = all_symbols[:] # this is to copy? because if there is a change in the orginal array it would effect
      for _ in range(rows):
          value = random.choice(current_symbols)
          current_symbols.remove(value)
          column.append(value)

      columns.append(column)

  return columns

# To print the slot machine to get a view
def print_slot_machine(columns):
  for row in range(len(columns[0])):
      for i, column in enumerate(columns):
          if i != len(columns) - 1:
              print(column[row], end=" | ")
          else:
              print(column[row], end="")

      print()

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

  slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
  print_slot_machine(slots)
  
main()
# Pyhton has no constant rule like JavaScript so we use naming rules of PEP 8
MAX_LINES = 3

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


def main():
  balance = deposit()
  lines = get_number_of_line()
  print(balance, lines)
main()
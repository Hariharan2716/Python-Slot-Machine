
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


deposit()



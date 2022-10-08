from replit import clear
from art import logo

print(logo)

bidders = {}
def bidding_function():
  name_input = str(input("What is your name?\n"))
  bid_price = int(input("How much are you bidding?\n$"))
  bidders[name_input] = bid_price
  # print(bidders)

bidding_function()

end = False
while not end:
  new_bid = input("Are there any other users who wish to bid? 'yes' or 'no'\n").lower()
  if new_bid == "yes":
    clear()
    print(logo)
    bidding_function()
  elif new_bid == "no":
    end = True
  else:
    print("Invalid input")

for name in bidders:
  highest_bid = 0
  winner = ""
  bid_value = bidders[name]
  if bid_value > highest_bid:
    highest_bid = bid_value
    winner = name

print(f"The winner of the silent auction is {winner} with $ {highest_bid}. Congratulations! ")



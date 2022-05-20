# Project 8
# The Secret Auction Program
from art import logo

# greet user
print(logo)
print("Welcome to the Secret Auction Program.")

# create bidder database
bids = {}

# loop to run through all bidders
bidding = True

while bidding:

    # ask name
    name = input("What is your name?\n")

    # ask bid amount
    bid = float(input("What is your bid amount?\n"))

    # make entry in database
    bids[name] = bid

    # ask if there are other bidders
    other_bidders = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()

    # break condition if no more bidders
    if other_bidders == 'yes':
        print("\n"*25)
    else:
        bidding = False

# find out the highest bidder
highest_bidder = ""
highest_bid = 0

for name in bids:
    if bids[name] > highest_bid:
        highest_bidder = name
        highest_bid = bids[name]

# print winner
print(f"{highest_bidder.capitalize()} wins the Secret Auction with a bid of ${highest_bid}.")

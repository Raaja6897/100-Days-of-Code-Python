from replit import clear
# HINT: You can call clear to

from art import logo
print(logo)

next = True
bid_dict={}

def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")

while next:
    name = str(input("What is your name"))
    bid = int(input("Enter the bid amount: $"))
    next = input("Is there a next audience, Yes or No\n").lower()
    bid_dict[name]= bid
    if next=="no":
        next=False
        find_highest_bidder(bid_dict)
        #print(bid_dict)
    elif next=="yes":
        clear()

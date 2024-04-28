# Create an empty dictionary
bids = {}
# Create a variable to check if there are other bidders 
other_bidders = True

# Create a function to find the highest bidder  
def highest_bidder(smth):
    starting_value=0
    for key in smth:
        current_bid=int(smth[key])
        if current_bid>starting_value:
            starting_value=current_bid
    print(f"Highest bid is {starting_value} made by {key}")
        
        
# Create a while loop to ask for the name and bid of the bidder
while other_bidders:
    name=input("what is your name \n")
    bid_amount=input("how much you bid \n")
    bids[name]=bid_amount
#     print(bids)  

# Ask if there are other bidders
    other_bidder=input("is there any other bidder? type Y/N \n").lower()
    if other_bidder=="n":
        other_bidders=False

highest_bidder(bids)
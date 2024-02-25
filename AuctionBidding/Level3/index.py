import os

dir_path = "./input"
files = os.listdir(dir_path)

for file in files:
    inputData = open(dir_path + "/" + file, "r").read().split(",")
    
    starting_bid = int(inputData[0])
    del inputData[0]

    current_bid = -1
    highestBidder = ""
    highestBid = -1
    
    priceHistory = f"-,{starting_bid}"

    for x in range(0, len(inputData), 2):
        bidder = inputData[x]
        price_bidded = int(inputData[x+1])
        
        if(bidder == highestBidder):
            highestBid = price_bidded
        elif(current_bid == -1):
            current_bid = starting_bid
            highestBid = price_bidded
            highestBidder = bidder
            priceHistory += f",{bidder},{current_bid}"
        elif(price_bidded > highestBid):
            current_bid = highestBid + 1
            highestBid = price_bidded
            highestBidder = bidder
            priceHistory += f",{bidder},{current_bid}"
        elif(price_bidded < highestBid):
            current_bid = price_bidded + 1
            priceHistory += f",{highestBidder},{current_bid}"
        else:
            current_bid = price_bidded
            priceHistory += f",{highestBidder},{current_bid}"
            
    print(priceHistory)
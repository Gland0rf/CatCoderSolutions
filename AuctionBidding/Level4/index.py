import os

dir_path = "./input"
files = os.listdir(dir_path)

for file in files:
    inputData = open(dir_path + "/" + file, "r").read().split(",")
    
    starting_bid = int(inputData[0])
    bin_price = int(inputData[1])
    del inputData[0:2]

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
            if(highestBid >= bin_price and price_bidded >= bin_price and bin_price != 0):
                current_bid = bin_price
                priceHistory += f",{highestBidder},{bin_price}"
                break
            current_bid = highestBid + 1
            highestBid = price_bidded
            highestBidder = bidder
            priceHistory += f",{bidder},{current_bid}"
        elif(price_bidded < highestBid):
            if(highestBid >= bin_price and price_bidded >= bin_price and bin_price != 0):
                current_bid = bin_price
                priceHistory += f",{highestBidder},{bin_price}"
                break
            current_bid = price_bidded + 1
            priceHistory += f",{highestBidder},{current_bid}"
        else:
            if(highestBid >= bin_price and price_bidded >= bin_price and bin_price != 0):
                current_bid = bin_price
                priceHistory += f",{highestBidder},{bin_price}"
                break
            current_bid = price_bidded
            priceHistory += f",{highestBidder},{current_bid}"
            
        
            
    print(priceHistory)
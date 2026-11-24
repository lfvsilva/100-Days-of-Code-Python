import subprocess


blind_auction = {}
print("Welcome to the secret auction program.")

is_to_continue = True
while is_to_continue:
    bidder_name = input("What is your name?: ")
    bid_value = float(input("What\'s your bid? $"))

    blind_auction[bidder_name] = bid_value

    continue_option = input("Are there any other bidders? Type \'yes\' or \'no\'.\n").lower()
    if continue_option == "yes":
        is_to_continue = True
        
    else:
        maxkey = max(blind_auction, key=blind_auction.get)
        is_to_continue = False
    subprocess.call("cls||clear", shell=True)

print(f"The winner is {maxkey} with a bid of ${blind_auction[maxkey]}")

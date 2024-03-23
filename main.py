import os
import auction_art

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
    
print(auction_art.logo)
    
user_name = input('Please Enter Your Name :\n')
user_bid = int(input('Please Enter Your Bid : \n$'))

user_log = {}
in_program = True

while in_program == True:
    user_log[user_name] = user_bid
    user_continue = input("Insert Another Bidder ? \n Type 'Yes' or 'No': \n").lower()
    clear_screen()
    
    if user_continue == 'yes':
        user_name = input('Please Enter Your Name : \n')
        user_bid = int(input('Please Enter Your Bid :\n$'))

        
    elif user_continue == 'no':
        max_value = max(user_log.values())
        for key,value in user_log.items():
            if value == max_value:
                print('')
                print(f"The highest bidder is {key} with ${value}")
                print('')
                print("Program End, Thank You")
                in_program = False
                
        
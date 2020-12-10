# bioThai
# 11/6/19
# Interest Calculator: Calculates interest on a loan.

#!/usr/bin/env python3

from decimal import Decimal
from decimal import ROUND_HALF_UP

#process input string (remove characters), return amount as decimal
def remove_chars(string_input):
    string_input = string_input.replace("$", "")
    string_input = string_input.replace(",", "")
    string_input = string_input.replace("%", "")
    if string_input.endswith("K") or string_input.endswith("k"):
        string_input = string_input.replace("K", "")
        string_input = string_input.replace("k", "")
        amount = 1000 * Decimal(string_input)
    else:
        amount = Decimal(string_input)
    return amount

#calculate interest amount
#Use quantize to round half up to 2 decimal places (0.005 rounds to 0.01)
def find_interest(loan_amount, interest_rate):
    interest = (interest_rate / 100) * loan_amount
    interest = interest.quantize(Decimal("0.00"), ROUND_HALF_UP)    
    return interest

def main():
    #display welcome message
    print("======= Interest Calculator =======")

    #simulate do-while loop
    repeater = "y"
    while repeater.lower() == "y":

        #prompt user for loan amount
        loan_string = str(input("\nEnter loan amount: "))
        loan_amount = remove_chars(loan_string)

        #prompt user for interest rate
        interest_rate_str = str(input("Enter interest rate: "))
        interest_rate = remove_chars(interest_rate_str)
            
        #get interest amount on loan
        interest_amt = find_interest(loan_amount, interest_rate)
        
        #format number of decimal places, add commas for every thousands place, convert decimals to strings, append $ or %
        loan_amount_formatted = "$" + "{:,.2f}".format(loan_amount)
        interest_rate_formatted = "{:,.3f}".format(interest_rate) + "%"
        interest_amt_formatted = "$" + "{:,.2f}".format(interest_amt)

        #print output and use left/right justification to align results
        print()
        print("Loan amount:".ljust(17), loan_amount_formatted.rjust(20))
        print("Interest rate:".ljust(17), interest_rate_formatted.rjust(20))
        print("Interest amount:".ljust(17), interest_amt_formatted.rjust(20))

        #repeat program as often as desired, based on user input, and validate input
        repeater = str(input("\nContinue? (y or n): "))
        while repeater.lower() != "y" and repeater.lower() != "n":
            repeater = str(input("  Please enter y or n: "))

    print("\nBye!")

if __name__ == "__main__":
    main()

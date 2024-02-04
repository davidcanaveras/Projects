import math 

# This is a program that calculates:
# 1. The earnings of an investment with simple or compund interest.
# 2. The monthly repayment needed for a home loan.


#First, user is asked for input to select either investment or bond calculator
while True:
    print("investment - to calculate the amout of interest you'll earn on your investment")
    print("bond       - to calculate the amount you'll have to pay on a home loan")
    
    # .lower funtion used to make the program not case sensitive as user may enter input in several different valid ways (e.g.INVESTMENT, Bond)
    selection = input("Enter either 'investment' or 'bond' to proceed: ")
    selection = selection.lower()

    # user selects investment
    if selection == "investment":
        
        # user is asked for input and it is cast into floats and integers to be able to calculate interest earned on the investment 
        deposit = float(input("How much money will you deposit?: "))
        interest_rate = float(input("How much interest will you be benefiting from? (as a percentage): "))
        years_investment = int(input("For how many years do you plan on investing?: "))
        # user is asked to select either simple or compound interest 
        interest = input("Would you like to get simple or compound interest?: ")
        interest = interest.lower()
        
        # when user selects simple interest, the following operation will be carried out and loop will cease after printing out total earnings
        if interest == "simple":
            # total amount after simple interest is earned on deposit is calculated
            deposit_plus_interest = deposit * (1 + (interest_rate/100) * years_investment)
            # interest earned over deposit is calculated
            interest_earned = deposit_plus_interest - deposit
            # total earnings are rounded up for clarity, leaving out any extra decimals which cannot be represented on money
            interest_earned = round(float(interest_earned))
            # interested earned on top of deposit is printed out. 
            # integers and floats previously used in calculation are cast into strings to be printed out
            print("In " + str(years_investment) + " years you will have earnt approximately " + str(interest_earned) + " pounds on top of your deposit")
            break
        
        # when user selects compound interest, the following operation will be carried out and loop will cease after printing out total earnings
        if interest == "compound":
            # total amount after compound interest is earned on deposit is calculated
            deposit_plus_interest = deposit * math.pow((1 + interest_rate/100),years_investment)
            # earnings over deposit are calculated
            interest_earned = deposit_plus_interest - deposit
            # total earnings are rounded up for clarity, leaving out any extra decimals which cannot be represented on money
            interest_earned = round(float(interest_earned))
            # total earnings are printed out
             # integers and floats previously used in calculation are cast into strings to be printed out
            print("In " + str(years_investment) + " years you will have earnt approximately " + str(interest_earned) + " pounds on top of your deposit")
            break
        
    # when user selects bond, they will be asked for input, which will be cast into floats to calculate montlhy repayment needed to pay back loan   
    elif selection == "bond":
        house_value = float(input("What's the house value?: "))
        interest_rate = float(input("What's the interest rate? (percentage): "))
        months_repayment = int(input("How long (in months) are you planning to take to repay the bond?: "))
        # monthly repayment is calculated
        total_repayment = ((interest_rate/100)/12 * house_value) / (1 - (1 + ((interest_rate/100)/12))**(-months_repayment))
        # monthly repayment is rounded up to leave out any extra decimal that can't be represented in real money
        total_repayment = round(total_repayment)
        # montlhy repayment is printed out
        # integers and floats previously used in calculation are cast into strings to be printed out
        print("You will have to pay approximately " + str(total_repayment) + "  pounds a month to repay the bond back in " + str(months_repayment) + " months")
        break
    
    # if user enter other that "investment" or "bond" (in any upper or lower case letters), the following message will be printed out and loop will restart.
    # when loop restarts, user will be asked to insert "investment" or "bond"
    else:
        print("sorry, invalid input")
        
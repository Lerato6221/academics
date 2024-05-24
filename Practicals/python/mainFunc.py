# This is a Demo for Def.
#The intention of this code is to allow #
# People to Register at a Mashonisa website, the their loan application wil be processed
# Based on the following criteria
#
# 0 They must register
# 1 They're over 18
# 2 They have a stable job.
# 3 They at least earn R13, 000 after tax
# 4 The site should calculate affordibility 
# 4 to qualify the client must be left with 7k

def mashonisa():

    def user_login():
        name = input("Please type your Name")
        surname = input("Please insert your Surname")
        age = int(input("Please insert your age"))


    
def loan_calc():
    # This is a take home salary
    amount = float(input("Please insert your salary below.\nR "))

    UIF = 177
    QUALUFYING_AMOUNT = 7000

    #This are amounts are we gonna minus from the salary
    car_amount = float(input("Please insert the car monthly installment\nR "))
    house_amount = float(input("Please insert rent/bond amount\nR "))
    medical_aid_amount = float(input("How much do you pay for Medical Aid\nR "))
    grocery_amount = float(input("Please insert the total estimate for groceries\nR "))

    monthly_total =  car_amount + house_amount +grocery_amount + medical_aid_amount

    total_total = monthly_total + UIF

    real_total = amount - total_total

    #Message to confirm the total amount
    print(f"The total amount for your monthly expenditure is R {monthly_total:,.2f}, meaning you have R{real_total:,.2f} left.")

    if real_total < QUALUFYING_AMOUNT  or real_total == QUALUFYING_AMOUNT:
        print(f"Apologies , You do not qualify for the Loan.")
    else:
        print(f"\nCongradulation sir. You do qualify for a loan amount of ''' ")


    
if __name__=='__main__':
    mashonisa()
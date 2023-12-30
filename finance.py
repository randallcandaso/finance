
print('''-----------------------------
----- WHERE'S THE MONEY -----
-----------------------------''')

annual = input('What is your annual salary?\n')

if annual.isnumeric() == False:
    print('Must enter positive integer for salary.')
    exit()
else: monthly = input('How much is your monthly mortgage or rent?\n')
if monthly.isnumeric() == False:
    print('Must enter positive integer for mortgage or rent.')
    exit()
else: bills = input('What do you spend on bills monthly?\n')
if bills.isnumeric() == False:
    print('Must enter positive integer for bills.')
    exit()
else: weekly = input('What are your weekly grocery/food expenses?\n')
if weekly.isnumeric() == False:
    print('Must enter positive integer for food.')
    exit()
else: travel = input('How much do you spend on travel annually?\n')
if travel.isnumeric() == False:
    print('Must enter positive integer for travel.')
    exit()

annual = int(annual)
monthly = int(monthly)
bills = int(bills)
weekly = int(weekly)
travel = int(travel)

if annual <= 15000:
    tax = 10
elif annual > 15000 and annual <= 75000:
    tax = 20
elif annual > 75000 and annual <= 200000:
    tax = 25
elif annual > 200000:
    tax = 30

tax = int(tax)
tax_limit = False

annual_tax = annual * (tax / 100)
if annual_tax >= 75000:
    annual_tax = 75000
    tax_limit = True
tax_percentage = (annual_tax / annual) * 100

annual_mortgage = monthly * 12
mortgage_percentage = (annual_mortgage / annual) * 100
annual_bills = bills * 12
bills_percentage = (annual_bills / annual) * 100
annual_food = weekly * 52
food_percentage = (annual_food / annual) * 100
travel_percentage = (travel / annual) * 100
annual_extra = (annual - (annual_mortgage) - (annual_bills) - (annual_food) - (travel) - (annual_tax))
annual_extra = int(annual_extra)
extra_percentage = (annual_extra / annual) * 100
line = max(int(mortgage_percentage), int(bills_percentage), int(food_percentage), int(travel_percentage), int(tax), int(extra_percentage))

print(' ')
print('------------------------------------------' + '-' * line)
print('See the financial breakdown below, based on a salary of $' + str(annual))
print('------------------------------------------' + '-' * line)
print('| mortgage/rent | $', format(annual_mortgage,'10,.2f'), '|', format(mortgage_percentage,'5,.1f') + '%', '|', '#' * int(mortgage_percentage))
print('|         bills | $', format(annual_bills,'10,.2f'), '|', format(bills_percentage,'5,.1f') + '%', '|', '#' * int(bills_percentage))
print('|          food | $', format(annual_food,'10,.2f'), '|', format(food_percentage,'5,.1f') + '%', '|', '#' * int(food_percentage))
print('|        travel | $', format(travel,'10,.2f'), '|', format(travel_percentage,'5,.1f') + '%', '|', '#' * int(travel_percentage))
print('|           tax | $', format(annual_tax,'10,.2f'), '|', format(tax_percentage, '5,.1f') + '%', '|', '#' * int(tax_percentage))
print('|         extra | $', format(annual_extra,'10,.2f'), '|', format(extra_percentage, '5,.1f') + '%', '|', '#' * int(extra_percentage))
print('------------------------------------------' + '-' * line)

if tax_limit == True:
    print('>>> TAX LIMIT REACHED <<<')
if annual_extra < 0:
    print('>>> WARNING: DEFICIT <<<')

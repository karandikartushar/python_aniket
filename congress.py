age=float(input('How old are you?'))
citizenship=float(input('No. of years you have been a US citizen?'))
if age>=30 and citizenship>9:
    print('You are eligible for both the House and Senate.')
elif age >=25 and age<30 and citizenship>=7 and citizenship<9:
    print('You eligible only for the House.')
else:
    print('You are ineligible for Congress.')

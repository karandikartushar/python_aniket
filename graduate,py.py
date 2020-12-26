def main():
    name=input('What is your name?')
    credit=int(input('How many credits do you have?'))
    if credit >= 120:
        print('Congratulations '+name+'! You have enough credits to graduate!')
    else:
        print('Sorry '+name+'. You do not have enough credits to graduate.')

main()

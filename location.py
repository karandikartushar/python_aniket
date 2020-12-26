def printlocations(sentence,letter):
    x = len(sentence)
    location = 0
    for i in range(x):
        location = sentence.find(letter,location)
        if location == -1:
            break
        print(location)
        location = location+1

s = input('Enter a sentence:')
l = input('enter the letter you want to find in your sentence:')
printlocations(s,l)

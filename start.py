def startsWithArticle(title):
    if title.startswith('There')==True:
         print('Program incomplete.Condition failed.')
    elif title.startswith('The')==True:
        print('Program complete.Condition succesful.')
    elif title.startswith('A')==True:
        print('Program complete.Condition succesful.')
    elif title.startswith('An')==True:
        print('Program complete.Condition succesful.')
    else:
        print('Program incomplete.Condition failed.')


startsWithArticle(input('Type a sentence.'))

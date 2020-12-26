print('Hello.')
print("Welcome to Anikait's Library.")
print('You can issue,return or add books.')
storage = ['the last olympian', 'the battle of the labyrinth', 'the sea of monsters', "the titan's curse",
           'the lightning thief', "the serpent's shadow", 'the blood of olympus', 'the house of hades',
           'the hidden oracle', 'dogs in the dead of night', 'the emerald atlas', 'the black reckoning',
           'secret of the unicorn', 'full circle', 'ghost wolf', 'cry of the wolf', 'the enchantress returns',
           'worlds collide', 'the wishing spell', 'the mountain of adventure', 'a tiny bit lucky', 'the temple tiger',
           'i am malala', 'secrets', 'auggie & me', 'wonder', 'oblivion', 'a grimm warning', 'frost like night',
           'snow like ashes', 'ice like fire', 'weird but true 2', '1001 inventions that changed the world',
           'ultimate family visual dictionary', 'murder on the orient express', 'shock for the secret seven',
           '100 and more logic and math puzzles', '100 logic & math brain teasers', '1001 amazing puzzles',
           'little women', 'pride and prejudice', 'the hunger games', 'catching fire', 'mockingjay', 'the fifth wave',
           "ender's game", 'devlok', 'the vedas and upanishads', 'pashu', 'percy jackson and the greek gods',
           'percy jackson and the greek heroes']
books = ['the last olympian', 'the battle of the labyrinth', 'the sea of monsters', "the titan's curse",
         'the lightning thief', "the serpent's shadow", 'the blood of olympus', 'the house of hades',
         'the hidden oracle', 'dogs in the dead of night', 'the emerald atlas', 'the black reckoning',
         'secret of the unicorn', 'full circle', 'ghost wolf', 'cry of the wolf', 'the enchantress returns',
         'worlds collide', 'the wishing spell', 'the mountain of adventure', 'a tiny bit lucky', 'the temple tiger',
         'i am malala', 'secrets', 'auggie & me', 'wonder', 'oblivion', 'a grimm warning', 'frost like night',
         'snow like ashes', 'ice like fire', 'weird but true 2', '1001 inventions that changed the world',
         'ultimate family visual dictionary', 'murder on the orient express', 'shock for the secret seven',
         '100 and more logic and math puzzles', '100 logic & math brain teasers', '1001 amazing puzzles',
         'little women', 'pride and prejudice', 'the hunger games', 'catching fire', 'mockingjay', 'the fifth wave',
         "ender's game", 'devlok', 'the vedas and upanishads', 'pashu', 'percy jackson and the greek gods',
         'percy jackson and the greek heroes']
authors = {
    'national geographic': ['weird but true 2'],
    'jack challoner': ['1001 inventions that changed the world'],
    'dk': ['ultimate family visual dictionary'],
    'agatha christie': ['murder on the orient express'],
    'enid blyton': ['shock for the secret seven', 'the mountain of adventure'],
    'rick riordan': ['the last olympian', 'the battle of the labyrinth', 'the sea of monsters', "the titan's curse",
                     'the lightning thief', "the serpent's shadow", 'the blood of olympus', 'the house of hades',
                     'the hidden oracle', 'percy jackson and the greek gods', 'percy jackson and the greek heroes'],
    'sara raasch': ['frost like night', 'snow like ashes', 'ice like fire'],
    'chris colfer': ['the enchantress returns', 'worlds collide', 'the wishing spell', 'a grimm warning'],
    'anthony horowitz': ['oblivian'],
    'r j palacio': ['wonder', 'auggie & me'],
    'jacqueline wilson': ['secrets'],
    'malala yousafzai': ['i am malala'],
    'l pichon': ['a tiny bit lucky'],
    'mary pope osborn': ['dogs in the dead of night'],
    'rachel roberts': ['secret of the unicorn', 'full circle', 'ghost wolf', 'cry of the wolf'],
    'john stephens': ['the emerald atlas', 'the black reckoning'],
    'scholastic': ['100 and more logic and math puzzles', '100 logic & math brain teasers'],
    'robert allen': ['1001 amazing puzzles'],
    'louisa m alcott': ['little woman'],
    'jane austen': ['pride and prejudice'],
    'suzanne collins': ['the hunger games', 'catching fire', 'mockingjay'],
    'rick yancey': ['the fifth wave'],
    'orson scott card': ["ender's game"],
    'devdutt pattanaik': ['devlok', 'the vedas and upanishads', 'pashu'],
}
genres = {'mylthological adventure': ['the last olympian', 'the battle of the labyrinth', 'the sea of monsters',
                                      "the titan's curse", 'the lightning thief', "the serpent's shadow",
                                      'the blood of olympus', 'the house of hades', 'the hidden oracle'],
          'magical adventure': ['the emerald atlas', 'the black reckoning', 'secret of the unicorn', 'full circle',
                                'ghost wolf', 'cry of the wolf', 'the enchantress returns', 'worlds collide',
                                'the wishing spell', 'a grimm warning'],
          'adventure': ['the mountain of adventure'],
          'historical adventure': ['dogs in the dead of night'],
          'knowledge': ['weird but true 2', '1001 inventions that changed the world',
                        'ultimate family visual dictionary'],
          'brain teasers': ['100 and more logic and math puzzles', '100 logic & math brain teasers',
                            '1001 amazing puzzles'],
          'sci-fi': ["ender's game", 'the fifth wave'],
          'mythology': ['devlok', 'the vedas and upanishads', 'pashu', 'percy jackson and the greek gods',
                        'percy jackson and the greek heroes'],
          'classics': ['little woman', 'pride and prejudice']
          }
again = 1
while again == 1:

    def check(book):
        num = 0
        for i in range(len(books)):
            if book != books[i]:
                num += 1
            else:
                return num


    def check_2(book):
        for i in range(len(books)):
            if book == books[i]:
                return True


    def title():
        z = input('Please enter a title:')
        q = 0
        for i in range(len(books)):
            if z == books[i]:
                q += 1
                print('We have this book.')
                print('book has been issued.')
                del books[i]
                break
        if q == 0:
            print('we do not have this book.')


    def author():
        r = 1
        d = input('Enter the author name:')
        print(authors[d])
        e = input('Enter the book name:')
        for i in range(len(authors[d])):
            if e == authors[d][i]:
                r += 1
                t = check_2(e)
                if t == True:
                    print('We have this book.')
                    print('book has been issued to you.')
                    l = check(e)
                    del books[l]
                else:
                    print('book has been issued to someone else')
                break
        if r == 0:
            print('We do not have this book.')


    def genre():
        g = 0
        h = input('Enter the genre:')
        print(genres[h])
        e = input('Enter the book name:')
        for x in range(len(genres[h])):
            if e == genres[h][x]:
                g += 1
                t = check_2(e)
                if t == True:
                    print('We have this book.')
                    print('book has been issued to you.')
                    l = check(e)
                    del books[l]
                else:
                    print('book has been issued to someone else')
            break
        if g == 0:
            print('We do not have this book.')


    def issue():
        b = 1
        while b == 1:
            y = input('How would you like to search?You can search by title,genre or author:')
            if y.lower() != 'title' and y.lower() != 'genre' and y.lower() != 'author':
                print('Invalid response.Please try again.')
                b = 1
            else:
                b += 1
        if y.lower() == 'title':
            title()
        if y.lower() == 'genre':
            genre()
        if y.lower() == 'author':
            author()


    def return_book():
        j = input('Name the book you want to return:')
        d = 0
        p = 0
        for i in range(len(storage)):
            if j == storage[i]:
                p += 1
                for n in range(len(books)):
                    if j == books[n]:
                        d += 1
                        print('This book is already with us.')
                if d == 0:
                    print('Book has been returned')
                    books.append(j)
        if p == 0:
            print('Please go to the addition section')


    def add():
        k = input('Please name the book you want to add to the library permanently:')
        d = input('Please name the author:')
        m = input('Please name the genre:')
        for i in range(len(authors)):
            if d == authors[i]:
                for v in range(len(authors[i])):
                    if k == authors[i][v]:
                        print('We already have this book.')
                    else:
                        authors.update({d: authors[d][v].append(k)})
            else:
                authors[d] = k
        for i in range(len(genres)):
            if d == genres[i]:
                for v in range(len(genres[i])):
                    if k == genres[i][v]:
                        print('We already have this book.')
                    else:
                        genres.update({d: genres[d][v].append(k)})
            else:
                genres[d] = k
        storage.append(k)
        books.append(k)
        print('Book has been added')


    a = 1
    while a == 1:
        x = input('How can I help you:')
        if x.lower() != 'issue' and x.lower() != 'return' and x.lower() != 'add':
            print('Invalid response.Please try again.')
            a = 1
        else:
            a += 1
    if x.lower() == 'issue':
        issue()
    if x.lower() == 'return':
        return_book()
    if x.lower() == 'add':
        add()
    qe = input('Anything else:')
    if qe.lower() == 'yes':
        again += 0
    if qe.lower() == 'no':
        again += 1
print('Thank you.Have a good day.')

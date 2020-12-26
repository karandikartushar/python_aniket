def main(words):
    a=words.split()
    print(a)
    b=a[::-1]
    x=' '.join(b)
    print(x)

main(input('Enter a sentence:'))
    

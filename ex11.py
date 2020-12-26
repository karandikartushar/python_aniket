def main():
    a=int(input('Enter a number:'))
    if a>=1:
      x=range(1,a)
      for num in x:
        if a%num==0:
            print('number is not prime')
            break
        else:
            print('number is prime')
            break
    else:
        print('invalid input')
main()

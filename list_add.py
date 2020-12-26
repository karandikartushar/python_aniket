def list_add(list1,value,index):
    if index>len(list1):
        print('Sorry.Cannot use index position.')
        print('program over.')
    if index<=len(list1):
        x=list1[index:]
        del list1[index:]
        list1.append(value)
        for z in range(0,len(x)):
            list1.append(x[z])
        return list1
    
def main():
    y=list_add(list(input('Enter a list without commas and spaces eg:"12345":')),input('Enter the element to put in the list:'),int(input('Enter the index position to put your element in the list:')))
    print(y)
main()

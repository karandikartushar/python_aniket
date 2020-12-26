def add_dictionary(dict1,dict2):
    dict3={}
    for key in dict1:
            dict3[key]=dict1[key]
    for key in dict2:
            dict3[key]=dict2[key]
    return dict3
        
def main():
    #dic1 = {[input('Enter a key:')] = input('Enter a value:'),[input('Enter a key:')]=input('Enter a value:'),[input('Enter a key:')]=input('Enter a value:')}
    #dic2 = {[input('Enter a key:')]=(input('Enter a value:')),[input('Enter a key:')]=input('Enter a value:'),[input('Enter a key:')]=input('Enter a value:')}
    print(add_dictionary(dic1,dic2))

#main()
dic1 = {[input('Enter a key:')] = input('Enter a value:')}


import os

while True:
    print("calculator")
    print('1. ➕') 
    print('2. ➖')
    print('3. ❌')
    print('4. exit') 
    ch = input('select a number >>>')
    if ch == '1':
        a = int(input("enter value 1:"))
        b = int(input('enter value 2:'))
        print (f'{a}+{b}={a+b}')
    elif ch == '2':
        pass
    elif ch == '3':
        pass
    elif ch == '4':
        print('bye!')
        break
    else:
        print('invalid input')
#si = p*r*r/100
p = int(input('principal is:'))
r = float(input('rate is :'))
t = int(input('time is'))
si =(p*r*t)/100
print("simple interest calc")
print(f'{p=}')
print(f'{r=}')
print(f'{t=}')
print(f'simple interest is ={si}')
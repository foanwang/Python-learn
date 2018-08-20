print('input 2 numbers:')
m = int(input('number1:'))
n = int(input('number2:'))
if m < n:
    m , n = n , m
while n != 0:
        r = m % n
        m = n
        n = r
if m == 1:
    print('Mutual!')
else:
    print('the biggest common factor', m)
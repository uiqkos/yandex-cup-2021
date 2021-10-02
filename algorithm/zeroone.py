
a = int(input().replace('one', '1').replace('zero', '0'))
b = int(input().replace('one', '1').replace('zero', '0'))

if a < b:
    print('<')
elif a > b:
    print('>')
else:
    print('=')

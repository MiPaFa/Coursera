tot = 0.0
num = 0

while True:
    sval = input('Enter a number: ')
    if sval == 'done':
        break
    try:
        fval = float(sval)
    except:
        print('Invalid input')
        continue
    tot = tot + fval
    num = num + 1
print (tot, num, tot / num)

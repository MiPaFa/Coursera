def computepay(h,r):
    if h <= 40:
        p = h * r
    else:
        p = 40 * r + ((h-40)*r) * 1.5
    return p

hrs = input('Enter Hours:\n')
rate = input('Enter Rate:\n')
try:
    h = float(hrs)
    r = float(rate)
except:
    print('please, please type in a correct number!')
    quit()

pay = computepay(h,r)
print(pay)

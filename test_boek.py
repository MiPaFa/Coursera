def computepay(h,r):
    if h <= 40:
        pay = h * r
    else:
        pay = 40 * r + ((h-40)*r) * 1.5
    return pay

hrs = input('Enter Hours:')
rte = input('Enter Rate:')
h = float(hrs)
r = float(rte)
antwoord = computepay(h,r)
print ('Pay:', antwoord)

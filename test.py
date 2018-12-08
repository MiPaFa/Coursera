astr = input('geef nummer in:')
try:
    istr = int(astr)
except:
    istr = -1

if istr > 0:
    print(istr, 'is inderdaad een nummer')
else:
    print('ik zeg geef een NUMMER in! <', astr, '> is geen nummer')
print ('done')

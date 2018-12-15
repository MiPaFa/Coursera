
prompt = 'geef een waarde in? '
x = input(prompt)
try:
    fx = int(x)
except:
    print(x, 'is geen cijfer')
    quit()
if fx%2 == 0:
    print (fx,'dit is een even getal')
else:
    print (fx,'dit is een oneven getal')

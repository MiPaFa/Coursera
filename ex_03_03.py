score = input("Enter Score: ")
try:
    fsc = float(score)
except:
    print ('please type valid score')
    quit()
if fsc > 1:
    print ('this is not a correct number')
elif fsc >=0.9:
    print ('A')
elif fsc >=0.8:
    print ('B')
elif fsc >=0.7:
    print ('C')
elif fsc >=0.6:
    print ('D')
else:
    print ('F')

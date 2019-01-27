# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
try:
    fh = open(fname)
except:
    exit()
count = 0
total = 0
for line in fh:
    line = line.rstrip()
    if not line.startswith("X-DSPAM-Confidence:") : continue
    line = line[20:]
    new = float(line)
    total = total + new
    count = count + 1
    #print(line)
    #print (total)
print('Average spam confidence:', total/count)

str = "X-DSPAM-Confidence:    0.8475"
ipos = str.find(':')
print(ipos)
piece = str[ipos+1:]
print(piece)
result = float(piece)
print(result)

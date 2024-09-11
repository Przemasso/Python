# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
spamCounter = 0
spamSum = 0
try:
    fh = open(fname)
except:
    print('Wrong file: ', fname)
    quit()

for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    else :
        spamCounter = spamCounter + 1
        digSearch = line.find(' ')
        digPos = line[digSearch +1:]
        digFloat = float(digPos)
        spamSum = spamSum + digFloat
avgSpam = spamSum/spamCounter
print("Average spam confidence:",avgSpam)

name = input("Enter file:")
# fuse for no filename
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
# opening new dictionary
counts = dict()
lst = list()
# loop through entered file
for line in handle:
# remove right blank space
    word = line.rstrip()
# check for particular lines 
    if word.startswith("From "):
# if line starts with From, split it to separate words
        senderLine = word.split()
# look for sender mail - second  
        senders = senderLine[1]
# build a list of senders
        lst.append(senders)
#print(lst)

# iterate through list of senders and create a dictionary of it
for sender in lst:
    counts[sender] = counts.get(sender, 0) +1
bignum = None
bigppl = None
for ppl,num in counts.items():
    if bignum is None or num > bignum:
        bignum = num
        bigppl = ppl
print(bigppl,bignum)
        





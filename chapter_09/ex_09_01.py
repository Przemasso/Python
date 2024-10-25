fname = input('Enter filename: ')
if len(fname) < 1: fname = "mbox-short.txt"

many = dict()
handle = open(fname)
for line in handle:
    line = line.rstrip()
    wds = line.split()
    for w in wds:
        many[w] = many.get(w, 0) +1
#print(many)

#find largest count
bigCount = None
bigWord = None

for key,value in many.items():
#    print(key, value)
    if bigCount is None or value > bigCount:
        bigCount = value
        bigWord = key
print(bigCount, bigWord)
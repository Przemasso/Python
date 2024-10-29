name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

hours_list = list()
for line in handle:
    line = line.rstrip()
    if line.startswith('From '):
        timestamp = line.split()
        hours = timestamp[5]
        #print(hours)
        colpos = hours.find(':')
        #print("Position of colon is:",colpos)
        hpos = hours[0 : colpos]
        #print("Hour only for this message is:", hpos)
        hours_list.append(hpos)

#print(hours_list)
hcount = dict()
for h in hours_list:
    hcount[h] = hcount.get(h, 0 ) + 1
#print(hcount)

for k,v in sorted(hcount.items()):
    print(k,v)
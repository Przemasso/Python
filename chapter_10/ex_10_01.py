fname = input('Enter filename: ')
if len(fname) < 1: fname = "clown.txt"

many = dict()
handle = open(fname)
for line in handle:
    line = line.rstrip()
    wds = line.split()
    for w in wds:
        many[w] = many.get(w, 0) +1
###
#find top 5 words by frequency
####

#prints dictionary        
#print(many)
#sorting only a keys of dictionary - list of a keys
#print(sorted(many))
#prints 2-tuples
#print(many.items())
#prints sorted 2-tuples
#print(sorted(many.items()))

tmp = dict()
newList = list()
#create key,value tuples
for k,v in many.items():
#print in value, key order
    tup = (v,k)
    newList.append(tup)
cool = sorted(newList, reverse=True)

for v,k in cool[:5]:
    print(k,v)
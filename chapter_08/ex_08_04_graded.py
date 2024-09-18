fname = input("Enter file name: ")
#empty list to fill in
lst = list()
try :
    fh = open(fname)
except:
    print('Invalid file name:', fname)
    quit()

for line in fh:
    line = line.rstrip()
#    print('Debug',line)
    words = line.split()
#    print('Debug:', words)
    for word in words:
        if not word in lst : lst.append(word)
#Because sort itself returns None
lst.sort()
print(lst)


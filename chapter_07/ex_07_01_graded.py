# Use words.txt as the file name
fname = input("Enter file name: ")
try:
    fh = open(fname)
except:
    print('File cannot be opened: ', fname)
    quit()
for word in fh:
    uword = word.upper()
#    strword = uword.rstrip()
#uword is a string variable and rstrip is a method
    print(uword.rstrip())
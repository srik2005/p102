def repcount():
    f = input("Enter File Path: ")
    g = input("Enter the Word you want to be counted: ")
    file = open(f,"r")
    nwords = 0
    for line in file:
        words = line.count(g)
        nwords = nwords + words
    print("No of times the word you entered repeated is  "+ str(nwords))

repcount()
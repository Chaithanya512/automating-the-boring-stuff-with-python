def commacode():
    spam = " "
    list = ['apples', 'bananas', 'tofu', 'cats', 'bacon']
    for i in list[:-1]:
        spam = spam + str(i) + ","
    if len(spam) != 0 :
        spam = str(spam) + 'and ' + str(list[-1])
        print(spam)
commacode()

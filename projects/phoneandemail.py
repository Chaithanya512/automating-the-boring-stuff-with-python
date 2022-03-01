import pyperclip, re
phoneregex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?  #area code
    (\s|-|\.)?   #seperator
    (\d{3})   #first 3 digits
    (\s|-|\.) # seperator
    (\d{4})  #last 4 digits
    (\s*(ext|x|ext.)\s*(\d{2,5})) # extension
    )''', re.VERBOSE)

# email regax
emailregex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+ #username
    @    # @ symbol
    [a-zA-Z0-9.-]+ #domain name
    (\.[a-zA-Z]{2,4})   #dot-something
    )''', re.VERBOSE)
#find matches in clipboard text.
text = str(pyperclip.paste())
matches = []
for groups in phoneregex.findall(text):
    phonenum = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] != '':
        phonenum +='x' + groups[8]
    matches.append(groups[0])

# copy results to the clipboard.
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('copied to clipboard:')
    print('\n'.join(matches))
else:
    print('no phone numbers or email adresses found.')



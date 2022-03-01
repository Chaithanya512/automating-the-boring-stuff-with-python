#Usage: py.exe mcb.pyw save <keyword> - saves clipboard to keyword.
#       py.exe mcb.pyw <keyword> - loads keyword to clipboard.
#       py.exe mcb.pyw list - loads all keywords to clipboard.
import pyperclip,shelve,sys
mcbshelf = shelve.open('mcb')
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcbshelf[sys.argv[2]] = pyperclip()
elif len(sys.argv) == 2:
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbshelf.keys())))
    elif sys.argv[1] in mcbshelf:
        pyperclip.copy(mcbshelf[sys.argv[1]])


mcbshelf.close()    
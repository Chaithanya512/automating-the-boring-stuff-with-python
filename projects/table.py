tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]
def printtable(tableData):
    colwidths = [0] * len(tableData)
    for i in range(len(tableData)):
        maxlen = [] + [len(tableData[i][j])]
        for j in range(len(tableData[i])):
            colwidths[i] = max(maxlen)
    
    for i in range(len(tableData[0])):
        for j in range(len(tableData[i])):
            print(tableData[i][j].rjust(colwidths[i]))
printtable(tableData)

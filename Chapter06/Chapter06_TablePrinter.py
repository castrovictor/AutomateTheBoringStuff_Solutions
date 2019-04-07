#Note: Assume that all the inner lists will contain the same number of strings

namesList = [['apples','oranges','cherries','bananas'],['Alice','Bob','Carol','David'],['dogs','cats','moose','goose']]

def printTable(tableData):
    colWidths = [0] * len(tableData)
    #Store the width of longest string in each list
    for i in range(len(colWidths)):
        colWidths[i] = len(max(tableData[i], key =len))

    maxWidth = max(colWidths)

    for i in range(0,len(tableData[0])):
        toPrint = ''
        for j in range(0,len(tableData)):
            toPrint += (tableData[j][i]).rjust(maxWidth)
        print(toPrint)


printTable(namesList)

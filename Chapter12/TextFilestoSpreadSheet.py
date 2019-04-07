"""Write a program to read in the contents of several text files (you can make
the text files yourself) and insert those contents into a spreadsheet, with
one line of text per row. The lines of the first text file will be in the cells of
column A, the lines of the second text file will be in the cells of column B,
and so on."""

import openpyxl, os, sys

nFiles = len(sys.argv)

#Create workbook
wb = openpyxl.Workbook()
sheet = wb.get_active_sheet()
sheet.title = "Text2Sheet"

# Load text files and save data
for i in range(1,nFiles):
    openFile = open(sys.argv[i])
    content = openFile.readlines()
    for line in range(len(content)):
        sheet.cell(row=line+1,column=i).value = content[line]

# Save Workbook
wb.save("Text2Sheet.xlsx")

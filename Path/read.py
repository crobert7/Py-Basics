strPath = 'Path/text.txt'

fileObject = open(strPath)
textList = fileObject.readlines()
fileObject.close()

for line in textList:
    print(line)

first_line = textList[0]
print(first_line)
second_line = textList[2]
print(second_line)
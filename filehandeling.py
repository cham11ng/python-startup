# File Handeling

text = 'This is really awesome.\nI am very happy.'

saveFile = open('exampleFile.txt', 'w')
saveFile.write(text)
saveFile.close()

appendText = '\nAlive is Awesome'

exampleFile = open('exampleFile.txt', 'a')
exampleFile.write(appendText)
exampleFile.close()

readExampleFile = open('exampleFile.txt', 'r')
print(readExampleFile.read())
# print(readExampleFile.readline())
# print(readExampleFile.readlines())


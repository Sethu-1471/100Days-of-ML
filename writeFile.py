text = "i write into file time"

saveFile = open("./example.txt", 'w')
saveFile.write(text)
saveFile.close()
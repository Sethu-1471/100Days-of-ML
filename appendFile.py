append = "\n i added third time \n new line"

appendfile = open("./example.txt", 'a')
appendfile.write(append)
appendfile.close()
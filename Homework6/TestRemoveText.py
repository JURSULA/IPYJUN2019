from RemoveText import RemoveText

filename = input("Enter the file name:")
word = input("Enter the string to be removed:")
rt = RemoveText(filename, word)
rt.removeText()
print("Done")

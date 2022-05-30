string = input("Introduce yourself: ")
characterCount= 0
wordCount=1
for i in string: 
    characterCount= characterCount+1
    if (i== " "):
        wordCount= wordCount+1

print("number of words in the string: ", wordCount)
print("number of characters in the string: ", characterCount)
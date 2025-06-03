# 1. Ask user for file name
filename = input("Enter the name of the file: ")

# 2. Try to open and read the file
try:
    with open (filename, 'r') as file:
        text = file.read()
except:
    print("File not found. Make sure the file exists in the same folder as this script.")
    exit()

# 3. Split into words (normalize to lowercase)
words = text.lower().split()

# 4. Create list of unique words
uniqueWords = []
for word in words:
    if word not in uniqueWords:
        uniqueWords.append(word)

# 5. Count word frequency using only
maxWord = ''
maxCount = 0

for word in uniqueWords:
    count = 0
    for w in words:
        if w == word:
            count += 1
    if count > maxCount:
        maxCount = count
        maxWord = word

# 6. Show the most repeated word
print(f"The most repeated word is '{maxWord}' ({maxCount} times)")
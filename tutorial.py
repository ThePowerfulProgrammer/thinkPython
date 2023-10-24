# Explain each line

wordCount = {}

with open("words.txt", "r") as file:
    for line in file:
        words = line.split()  
        for word in words:
            if word in wordCount:
                wordCount[word] += 1
            else:
                wordCount[word] = 1

most_common_word = max(wordCount, key=wordCount.get)

print("Most common word:", most_common_word)
print("Count:", wordCount[most_common_word])

import shelve
# Write a module that provides two new functions: store_an 
# agrams should store the anagram dictionary in a “shelf;” read_anagrams should look 
# up a word and return a list of its anagrams.

# Read a list of words and create a dict
# key = word, value = list of anagrams based on word
# DS only contains 1 k:v pair for each anagram set.

anagram = {}
with open("wordsForAnagram.txt", "r") as rFile:
    all_words = rFile.readlines()  # Read all lines from the file into a list

for word in all_words:
    #print(word, "1")
    # Read in word
    if word not in anagram:
        # Remove whitespace
        cleanedWord = word.strip()
        # Loop over all words again and determine which words are anagrams, then store in a list and the list is the corresponding value
        cleanedWordAnagrams = []
        for newWord in all_words:  # Use the list instead of iterating over the file again
            #print(newWord, "2")
            # Check length
            if len(newWord.strip()) == len(cleanedWord):
                charCount = 0
                # Check character
                for char in newWord.strip():
                    if char in cleanedWord:
                        charCount += 1
                # Condition to add to list of anagrams based on word
                if charCount == len(cleanedWord):
                    cleanedWordAnagrams.append(newWord.strip())

        # word:anagrams
        if cleanedWordAnagrams not in anagram.values():
            anagram[cleanedWord] = cleanedWordAnagrams
                            
            


# Write to file for reference    
with open("anagrams.txt", "w") as wFile:
    for k, v in anagram.items():
        # Convert the list of anagrams to a comma-separated string
        anagram_str = ", ".join(v)
        # Write the key-value pair to the file
        wFile.write(f"{k}: {anagram_str}\n")
        

# store_an_agrams should store the anagram dictionary in a “shelf;”  Write data to a shelve

def store_anagrams(dict):
    with shelve.open("anagramShelve") as db:
        for k,v in dict.items():
            db[k] = v
    return None

store_anagrams(anagram)

def read_anagrams(shelf:shelve):
    with shelve.open(shelf) as db:
        wordSearch = input("Enter a key to search: ")
        if wordSearch in db.keys():    
            print(f"--> {wordSearch}: {db[wordSearch]}")
        else:
            print("Word search error, check spelling, or key existance")
    return None

print(read_anagrams("anagramShelve"))
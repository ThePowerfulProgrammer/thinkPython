import os

'''
Write a function that reads the words in words.txt and stores them as keys in a dic
tionary. It doesnt matter what the values are. Then you can use the in operator as a fast 
way to check whether a string is in the dictionary
'''
def txtToDict(fileName):
    txtDict = {}
    try:
        with open(fileName, 'r') as file:
            for line in file:
                words = line.split();
                for word in words:
                    if word in txtDict:
                        txtDict[word] +=1;
                    else:
                        txtDict[word] = 1;
    except FileNotFoundError:
        print("File not found");                
    return txtDict;


file = input("Enter file name: ");
file_path = os.path.join(os.getcwd(), file)

print(txtToDict(file_path));
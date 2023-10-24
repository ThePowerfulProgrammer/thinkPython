import os
# Write a function called sed that takes as arguments a pattern string, a replacement string, 
# and two filenames; it should read the first file and write the contents into the second file 
# (creating it if necessary). If the pattern string appears anywhere in the file, it should be 
# replaced with the replacement string.
# If an error occurs while opening, reading, writing or closing files, your program should 
# catch the exception, print an error message, and exit.

def sed(pattern:str,replacement:str,file1,file2):
    try:
        # Read file 1 write to file 2
        with open(file1,"r") as file:
            
            
            with open(file2,"w") as writeFile:
                for line in file:
                    writeFile.write(line)        
    except:
        print("File does not exist")
        exit()
        
    # Check file 2 for occurences of pattern -> if true: replace pattern with replacement
    try:
        with open(file2, "r+") as file:
            fileRead = file.read()
            if pattern in fileRead:
                newFile = fileRead.replace(pattern, replacement)
                file.seek(0)
                file.write(newFile)
                file.truncate()
    except FileNotFoundError:
        print("File not found")
    except Exception as e:
        print("File read/write error:", str(e))
        exit()
    return "SUCCESS";

print(sed(" is"," REPLACEDDDDDDDDDDd","words.txt","copy.txt"))
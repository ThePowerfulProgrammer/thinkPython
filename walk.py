import os


def walk(directory):
    # Grab each file/folder in directory
    for name in os.listdir(directory):
        # Append the name to the path
        path = os.path.join(directory,name)
        
        # Use the os.path.isfile() --> true , we print
        if os.path.isfile(path):
            print(path)
        else:
            walk(path)
    return "DONE"
    
# Grab current dir
currentDir = os.getcwd();
print("Notice we will append to --->",currentDir, "\n")
print(walk(currentDir))
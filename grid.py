
# Write a function that draws a grid like the following:
# + - - - - + - - - - +
# |         |         |
# |         |         |
# |         |         |
# |         |         |
# + - - - - + - - - - +
# |         |         |
# |         |         |
# |         |         |
# |         |         |
# + - - - - + - - - - +


def generateGrid(side):
    for i in range(side):
        if i == 0 or i == int(side/2) or i == side-1:
            for j in range(side):
                if j == 0 or j == int(side/2) or j == side-1:
                    print("+ ",end="")
                else:
                    print("- ",end="")
        else:
            # Code for even vs odd side
            if (side%2 == 0):
                if i == 1 or i == int((side/2)+1):
                    print("")   
                print("|", " "*(int(side-3)), "|"," "*(int(side-5)), "|" )
            else:   
                if i == 1 or i == int((side/2)+1):
                    print("")   
                print("|", " "*(int(side-4)), "|"," "*(int(side-4)), "|" )
    print(" ")
    return f"A grid of size {side}x{side}";

print(generateGrid(side=17));
            
    
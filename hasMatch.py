# Given 2 tuples, determine the tuples have any element in common
def has_match(t1:tuple,t2:tuple):
    for elT1,elT2 in zip(t1,t2):
        if elT1 == elT2:
            return True
    return False


print(has_match((1,2,3), (4,5,3)))
print(has_match((1,2,3), (4,5,6)))
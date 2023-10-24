import pickle

'''
You can use pickle to store non-strings in a database. In fact, this combination is so 
common that it has been encapsulated in a module called shelve
'''

nums = [1,2,3]
# Any type to pickled type
pickled = pickle.dumps(nums)
print(pickled)

# Pickled type to original type
unpickled = pickle.loads(pickled)
print(unpickled)

# BUT :)
print(unpickled==nums)
print(unpickled is nums)
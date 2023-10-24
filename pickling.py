# Create a db using pickle methods
import pickle

# Sample data 
data  = {
    "name": "Ashish",
    "age": 22,
    "scores": [75,65,90]
}

# Step 1: Serialise the data
pickled_Data = pickle.dumps(data)

# View our data if we wish
# print(pickled_Data)

# Step 2: Write pickled data to db file
with open("pickleDataBase.db", "wb") as file:
    file.write(pickled_Data)
    
# Step 3: Read pickled data from file, deserialise and print
with open("pickleDataBase.db", "rb") as file:
    loaded_data = pickle.load(file)
    
    
print(loaded_data)

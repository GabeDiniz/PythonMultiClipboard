import sys
import clipboard
import json

SAVED_DATA = "clipboard.json"

def save_data(filepath, data):
    with open(filepath, 'w') as f:
        json.dump(data, f)

def load_data(filepath):
    try:
        with open(filepath, 'r') as f:
            data = json.load(f)
            return data
    except:
        return {}

def delete_data(filepath, key):
    with open(filepath, 'r') as old_data:
        data = json.load(old_data)
    del data[key]
    with open(filepath, 'w') as new_data:
        data = json.dump(data, new_data)
        

if len(sys.argv) == 2:
    command = sys.argv[1]
    data = load_data(SAVED_DATA)

    if command == "save":
        print("You're copying: ", clipboard.paste())
        key = input("Enter a key: ")
        data[key] = clipboard.paste()
        save_data(SAVED_DATA, data)
        print("Data saved!")
    
    elif command == "load":
        key = input("Enter a key: ")
        if key in data:
            clipboard.copy(data[key])
            print("Data copied to clipboard.")
        else:
            print("Key does not exist.")
    
    elif command == "list":
        print(data)
    
    elif command == "delete":
        print(data)
        key = input("Enter the key to be deleted: ")
        if key in data:
            delete_data(SAVED_DATA, key)
            print("test")
        else:
            print("key does not exist")
    
    else:
        print("Unknown command")
else:
    print("Please pass exactly one command.")


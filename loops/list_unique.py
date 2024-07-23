items = ["apple", "banana", "orange", "apple", "banana"]

# get unique items from this list

unique_items = set()

for item in items:
    if (item not in unique_items):
        print(f"Duplicate item {item}")
        continue
    
    unique_items.add(item)
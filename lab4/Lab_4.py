user_data = {}

user_count = int(input("Enter the number of users: "))

for i in range (user_count):
    user = input("Enter username: ")
    item_count = int(input("Enter the number of items: "))
    items = []

    for j in range (item_count):
        item = input("Enter item: ")
        items.append(item)

    user_data[user] = items

item_counts = {}
for items in user_data.values():
    for item in items:
        item_counts[item] = item_counts.get(item, 0) + 1

common_items = {item for item, count in item_counts.items() if count > 1}
unique_items = {item for item, count in item_counts.items() if count == 1}
max_count = max(item_counts.values())
most_popular = {item for item, count in item_counts.items() if count == max_count}

print("\nUSER DATA:")
for user, items in user_data.items():
    print(f"{user} -> {items}")

print("\nCOMMON ITEMS:")
for item in common_items:
    print(item)

print("\nUNIQUE ITEMS:")
for item in unique_items:
    print(item)

print("\nMOST POPULAR ITEM:")
for item in most_popular:
    print(item)
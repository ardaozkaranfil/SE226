user_data = {}

num_users = int(input("Enter number of users: "))

for i in range(num_users):
    username = input("Enter username: ")
    num_items = int(input("How many items? "))
    items = []
    for j in range(1, num_items + 1):
        item = input(f"Item {i}: ")
        items.append(item)
    user_data[username] = items

item_counts = {}
for items in user_data.values():
    for item in items:
        item_counts[item] = item_counts.get(item, 0) + 1

common_items = set()
unique_items = set()
most_popular = set()

max_count = max(item_counts.values())

for item, count in item_counts.items():
    if count > 1:
        common_items.add(item)
    else:
        unique_items.add(item)
    if count == max_count:
        most_popular.add(item)

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
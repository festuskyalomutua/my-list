my_list = []

# 2. Appending elements 10, 20, 30, 40
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

# 3. Inserting 15 at the second position (index 1)
my_list.insert(1, 15)

# 4. Extending with [50, 60, 70]
my_list.extend([50, 60, 70])

# 5. Removing the last element
my_list.pop()

# 6. Sorting in ascending order
my_list.sort()

# 7. Finding and printing index of value 30
index_of_30 = my_list.index(30)
print("Index of 30:", index_of_30)

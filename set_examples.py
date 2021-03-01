list1 = ['red', 'blue', 'purple', 'blue', 'blue', 'green', 'orange']
list2 = ['blue', 'green', 'green', 'purple', 'lavender', 'black', 'brown', 'pink']

set1 = set(list1)
set2 = set(list2)
print(set1)
print(set2)

print("common:", set1 & set2)  # intersection
print("only one:", set1 ^ set2)  # Xor
print("either:", set1 | set2)  # union
print("just set1:", set1 - set2)
print("just set2:", set2 - set1)
print(len(set1), len(set2))

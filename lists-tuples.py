# Tuples

x = 4, 5, 7, 2, 4
# or  y = (5, 4, 3, 2, 3)
print('Get Tuple:', x, x[2:])

# Lists


z = [2, 2, 6, 8, 8]
print('Get Lists:', z, z[2:])

z.append(5)
z.insert(2, 100)
z.remove(8)
print('After List Manipulation:', z)
print('Total 2:', z.count(2))

z.sort()
print('After Sorting:', z)

multi_dimensional_lists = [
    [3, 5],
    [5, 8],
    [5, 9]
]

print(multi_dimensional_lists[1][1])

"""
# display pattern
1
11
111
1111
11111
"""

total = 5
pattern = 1

for i in range(total):
    for j in range(i+1):
        print(1, end='')

    print()

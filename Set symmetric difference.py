print("Problem A")
set_a1 = {'blue', 'green'}
set_a2 = {'blue', 'yellow'}

symmetric_diff_a = set_a1.symmetric_difference(set_a2)

print(f"Set 1: {set_a1}")
print(f"Set 2: {set_a2}")
print(f"Symmetric Difference: {symmetric_diff_a}")
print("-" * 20)

print("Problem B")
set_1 = {1, 2, 3, 4, 5}
set_2 = {1, 5, 6, 7, 8, 9}

symmetric_diff_b = set_1 ^ set_2

print(f"Set 1: {set_1}")
print(f"Set 2: {set_2}")
print(f"Symmetric Difference: {symmetric_diff_b}")
print("-" * 20)
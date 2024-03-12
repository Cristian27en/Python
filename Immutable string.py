# Initial string
original_string = "Hello, World!"

# Concatenation
concatenated_string = original_string + " Welcome"
print("Original String:", original_string)
print("Concatenated String:", concatenated_string)

# Slicing
sliced_string = original_string[1:5]
print("Sliced String:", sliced_string)

# Replacing
replaced_string = original_string.replace("Hello", "Hi")
print("Original String:", original_string)
print("Replaced String:", replaced_string)

# If strings were mutable, you would expect the original string to be modified in each case.
# Because strings are immutable
# New string objects are created with the desired changes,
# Leaving the original string unchanged.

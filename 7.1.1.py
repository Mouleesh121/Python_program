a = input("Enter a string: ")

frequency = {}

for char in a:
    if char in frequency:
        frequency[char] += 1
    else:
        frequency[char] = 1

print("\nThe frequency of each character in the string is:")
for char, freq in frequency.items():
    print(f"'{char}': {freq}")
    


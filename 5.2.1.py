
n = int(input("Enter the number of elements: "))

arr = []

print("\nEnter the elements:")
for i in range(n):
    arr.append(int(input()))

unique = list(set(arr))

print("The unique elements in the array are:")
print(' '.join(map(str, unique)))


